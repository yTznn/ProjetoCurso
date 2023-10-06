from fastapi import APIRouter, HTTPException
from typing import List  # Importe List

from ModeloCursos import Curso

curso_router = APIRouter()

class CursoRouter:
    cursos = []

@curso_router.get("/cursos/", response_model=List[Curso])  # Use List[Curso]
async def get_cursos():
    return CursoRouter.cursos

@curso_router.get("/cursos/{curso_id}/", response_model=Curso)
async def get_curso_id(curso_id: int):
    if curso_id < 0 or curso_id >= len(CursoRouter.cursos):
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    
    return CursoRouter.cursos[curso_id]

@curso_router.post("/cursos/", response_model=Curso)
async def post_curso(curso: Curso):
    CursoRouter.cursos.append(curso)
    return curso

@curso_router.put("/cursos/{curso_id}/", response_model=Curso)
async def put_curso(curso_id: int, novo_curso: Curso):
    if curso_id < 0 or curso_id >= len(CursoRouter.cursos):
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    
    CursoRouter.cursos[curso_id] = novo_curso
    return novo_curso

@curso_router.delete("/cursos/{curso_id}/", response_model=Curso)
async def delete_curso(curso_id: int):
    if curso_id < 0 or curso_id >= len(CursoRouter.cursos):
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    
    curso_removido = CursoRouter.cursos.pop(curso_id)
    return curso_removido