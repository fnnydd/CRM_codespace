from abc import ABC, abstractmethod

from repository.any_kind_of_repo import TeacherRepository


class StudentABC(ABC):
    @abstractmethod
    async def check_teacher(self, first_name: str, last_name: str, email: str) -> bool: pass
    
    @abstractmethod
    async def add_teacher(self, first_name: str, last_name: str, email: str) -> bool: pass

    @abstractmethod
    async def get_teacher(self, staff_id: int): pass
    
    @abstractmethod
    async def change_teacher(self, first_name: str, last_name: str, email: str) -> bool: pass
    
    @abstractmethod
    async def remove_teacher(self, first_name: str, last_name: str, email: str) -> bool: pass
    

class Teacher(StudentABC):
    @classmethod
    def check_teacher(self, first_name: str, last_name: str, email: str) -> bool:
        return TeacherRepository().check_teacher(first_name=first_name, last_name=last_name, email=email)
    @classmethod
    def add_teacher(self, first_name: str, last_name: str, email: str) -> bool:
        return TeacherRepository().add_teacher(first_name=first_name, last_name=last_name, email=email)
    @classmethod
    def get_teacher(self, staff_id: int) -> bool:
        return TeacherRepository().get_teacher(staff_id=staff_id)
    @classmethod
    def change_teacher(self, first_name: str, last_name: str, email: str) -> bool:
        return TeacherRepository().change_teacher(first_name=first_name, last_name=last_name, email=email)
    @classmethod
    def remove_teacher(self, first_name: str, last_name: str, email: str) -> bool:
        return TeacherRepository().remove_teacher(first_name=first_name, last_name=last_name, email=email)
    