from fastapi import FastAPI

from service.any_kind_of_service import Teacher

app = FastAPI()

@app.get("/check_teacher/{first_name}, {last_name}, {email}")
async def root(first_name: str, last_name: str, email: str):
    return Teacher.check_teacher(first_name=first_name, last_name=last_name, email=email)

@app.get("/add_teacher/{first_name}, {last_name}, {email}")
async def root2(first_name: str, last_name: str, email: str):
    return Teacher.add_teacher(first_name=first_name, last_name=last_name, email=email)

@app.get("/get_teacher/{staff_id}")
async def root3(staff_id: int):
    return Teacher.get_teacher(staff_id=staff_id)

@app.get("/change_teacher/{first_name}, {last_name}, {email}")
async def root4(first_name: str, last_name: str, email: str):
    return Teacher.change_teacher(first_name=first_name, last_name=last_name, email=email)

@app.get("/remove_teacher/{first_name}, {last_name}, {email}")
async def root5(first_name: str, last_name: str, email: str):
    return Teacher.remove_teacher(first_name=first_name, last_name=last_name, email=email)


