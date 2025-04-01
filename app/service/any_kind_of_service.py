from abc import ABC, abstractmethod

from repository.any_kind_of_repo import TeacherRepository


class StudentABC(ABC):
    @abstractmethod
    async def add_teacher(self, name: str): pass

    @abstractmethod
    async def get_teacher(self, name: str) -> bool: pass


class Teacher(StudentABC):
    @classmethod
    def add_teacher(self, tg_id: int) -> bool:
        return TeacherRepository().add_teacher(tg_id=tg_id)
    @classmethod
    def get_teacher(self, tg_id: int) -> bool:
        return TeacherRepository().get_teacher(tg_id=tg_id)

