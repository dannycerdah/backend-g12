from flask import request
from flask_restful import Resource
from models.preparaciones import Preparacion
from dtos.preparacion_dto import PreparacionRequestDTO, PreparacionResponseDTO
from config import conexion

class PreparacionesController(Resource):
    def post(self):
        try:
            body = request.get_json()
            data = PreparacionRequestDTO().load(body)
            print(data)
            nuevaPreparacion=Preparacion(**data)
            conexion.session.add(nuevaPreparacion)
            conexion.session.commit()
            respuesta = PreparacionResponseDTO().dump(nuevaPreparacion)

            return {
                'message':'Preparacion creada exitosamente',
                'preparacion': respuesta
            },201
        except Exception as e:
            return {
                'message':'Hubo un error al crear la preparacion',
                'content': e.args
            }, 400
    
    def get(self):
        preparacion = conexion.session.query(Preparacion).filter_by(id=1).first()
        print(preparacion)
        print(preparacion.orden)
        print(preparacion.receta.nombre)
        print(preparacion.receta_id)

        return {
            'message':'ok'
        }