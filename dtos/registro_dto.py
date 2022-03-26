from config import validador
from models.usuarios import Usuario

class RegistroDto(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        