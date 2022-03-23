from flask_restful import Resource, request
from models.recetas import Receta
from dtos.receta_dto import RecetaPreparacionResponseDTO, RecetaRequestDTO, RecetaResponseDTO,BuscarRecetaRequestDto
from dtos.paginacion_dto import PaginacionRequestDTO
from config import conexion
from math import ceil 

# CREATE, GET ALL (PAGINATED), UPDATE, FIND por like de nombre, DELETE
class RecetasController(Resource):
    def post(self):
        body = request.get_json()
        try:
            data = RecetaRequestDTO().load(body)
            # creamos la instancia de la nueva receta PERO no la agregamos a la base de datos
            nuevaReceta = Receta(
                nombre = data.get('nombre'), 
                estado = data.get('estado'), 
                comensales=data.get('comensales'), 
                duracion=data.get('duracion'), 
                dificultad = data.get('dificultad') 
                )
            conexion.session.add(nuevaReceta)
            # https://docs.sqlalchemy.org/en/14/orm/session_api.html#sqlalchemy.orm.Session.commit
            # recien al hacer commit asignara el id correspondiente
            conexion.session.commit()
            respuesta = RecetaResponseDTO().dump(nuevaReceta)

            return {
                'message': 'Receta creada exitosamente',
                'content': respuesta
            }, 201

        except Exception as e:
            # https://docs.sqlalchemy.org/en/14/orm/session_api.html#sqlalchemy.orm.Session.rollback
            conexion.session.rollback()
            return {
                'message': 'Error al crear la receta',
                'content': e.args
            }
    
    def get(self):
        # TODO: agregar paginacion
        query_params = request.args
        paginacion = PaginacionRequestDTO().load(query_params)

        perPage = paginacion.get('perPage')
        page = paginacion.get('page')
        
        if(perPage < 1 or page < 1 ):
            return {
                'message':'los parametros no pueden recibir valores negativos'
            }, 400

        skip = perPage * (page - 1)

        recetas = conexion.session.query(Receta).limit(perPage).offset(skip).all()

        total = conexion.session.query(Receta).count()

        itemsXPage = perPage if total >= perPage else total
        totalPages = ceil(total/itemsXPage) if itemsXPage>0 else None
        prevPage =page - 1 if page > 1 and page <= totalPages else None
        nextPage = page + 1 if totalPages > 1 and page < totalPages else None


        respuesta = RecetaResponseDTO(many=True).dump(recetas)
        return {
            'message': 'Las recetas son:',
            'pagination': {
                'total': total,
                'itemsXPage': itemsXPage,
                'totalPage' : totalPages,
                'prevPage': prevPage,
                'nextPage': nextPage
                },
            'content': respuesta
        }

class BuscarRecetaController(Resource):
    def get(self):
        query_params = request.args
        try:
            parametros = BuscarRecetaRequestDto().load(query_params)   
            print(parametros)
            nombre = parametros.get('nombre','')
            if parametros.get('nombre') is not None:
                del parametros['nombre']
            # recetas2 = conexion.session.query(Receta).filter(Receta.nombre.like('%a%')).all()
            # recetas = conexion.session.query(Receta).filter_by(**parametros).all()
            recetas = conexion.session.query(Receta).filter(Receta.nombre.like('%{}%'.format(nombre))).filter_by(**parametros).all() 
            resultado = RecetaResponseDTO(many=True).dump(recetas)
            print(recetas)
            return{
                'message':'',
                'content': resultado
            }        
        except Exception as e:
             return{
                 'message':'Error al hacer la busqueda',
                 'content':e.args
             },400   


class RecetaController(Resource):
    def get(self, id): 
        receta: Receta | None = conexion.session.query(Receta).filter(Receta.id==id).first()
        if receta is None:
            return {
                'message': 'Rceta no encontrada'
            },404
        else:
            print(receta.preparaciones)
            respuesta = RecetaPreparacionResponseDTO().dump(receta)
            return {
                'message' : 'Receta encontrada',
                'content': respuesta
            },200 