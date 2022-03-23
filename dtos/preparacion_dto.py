from pyexpat import model
from statistics import mode
from xml.etree.ElementInclude import include
from config import validador
from models.preparaciones import Preparacion
from models.recetas import Receta
from marshmallow import fields



class PreparacionRequestDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Preparacion
        include_fk = True

class RecetaResponseDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Receta

class PreparacionResponseDTO(validador.SQLAlchemyAutoSchema):
    receta = fields.Nested(nested=RecetaResponseDTO, data_key='receta_relacion')
    class Meta:
        model = Preparacion
        load_instance=True
        include_fk = True
        include_relationships = True