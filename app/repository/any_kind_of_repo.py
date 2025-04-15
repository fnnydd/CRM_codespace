# repositories/abstract.py
from abc import ABC, abstractmethod


class StudentRepositoryABC(ABC):
    @abstractmethod
    def add_teacher(self, tg_id):
        pass

    @abstractmethod
    def get_teacher(self, tg_id):
        pass

