from pydantic import BaseModel, EmailStr


class UsuarioValidate(BaseModel):
    correo: EmailStr
    contraseña: str

    class Config:
        from_attributes = True
