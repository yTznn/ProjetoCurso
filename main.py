from fastapi import FastAPI
from rotasCurso import curso_router

app = FastAPI(
    title="API - Cursos",
    description="Api de cursos criada para a prova de POO II"
)

# Inclua os roteadores para cada recurso
app.include_router(curso_router, prefix="/Cursos")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)