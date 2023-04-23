from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel
app=FastAPI()
"""
GET - get data
POST - create data
PUT - update data
DELETE - delete data


"""
students={
    1:{
    "name":"Salah",
    
    "School":"MSA",
    "age":1

    },
      2:{
    "name":"CaPO",
    
    "School":"MSA",
    "age":30


    }
}
class Student(BaseModel):
    name:str
    School:str
    age:int
class student_update(BaseModel):
    name:Optional[str]=None
    School:Optional[str]=None
    age:Optional[int]=None
@app.get("/")
def index():
    return {"name":"Mohamed"}
@app.get("/get-students/{student_id}")
def get_student(student_id:int=Path(description="The ID of the desired student",gt=0)):
 
   return students[student_id]
@app.get("/students-by-name")
def byname(name:Optional[str]=None):
    for student in students:
        if students[student]['name']==name:
            return students[student]
    return "NOT FOUND"
@app.post("/add-student/{student_id}")
def add(student_id:int,student:Student):
    if student_id in students.keys():
       
            return{"ERROR":"already exist"}
    students[student_id]=student
    return "added successfully"
@app.get("/all-students")
def getAll():
    return students
@app.put("/update-students/{student_id}")
def update(student_id:int,student:student_update):
    if student_id not in students:
        return{"Error":"DOESN'T EXIST"}
    if student.name:
        students[student_id]["name"]=student.name
    if student.age:
        students[student_id]["age"]=student.age
    if student.School:
        students[student_id]["Schoo;"]=student.School

    
    
    
    return"updated successfully"
@app.delete("/delete-student/{student_id}")
def Delete(student_id:int):
    if student_id in students:
        del students[student_id]
        return "deleted successfully"
    
    return{"ERROR":"DOESN'T EXIST"}