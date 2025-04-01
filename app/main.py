from fastapi import FastAPI

from service.any_kind_of_service import Teacher

app = FastAPI()

@app.get("/add_teacher/{tg_id}")
async def root(tg_id: int):
    return Teacher.add_teacher(tg_id=tg_id)


@app.get("/get_teacher/{tg_id}")
async def say_hello(tg_id: int):
    return Teacher.get_teacher(tg_id=tg_id)


