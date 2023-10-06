from pydantic import BaseModel

class Curso(BaseModel):
    id: int
    titulo: str
    aulas: int
    hora: str
    dia: str