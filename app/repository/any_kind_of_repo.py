# repositories/abstract.py
import psycopg2
from config.config import DB_CONFIG
from abc import ABC, abstractmethod


class StudentRepositoryABC(ABC):
    @abstractmethod
    def check_teacher(self, first_name, last_name, email):
        pass
    @abstractmethod
    def add_teacher(self, first_name, last_name, email):
        pass
    @abstractmethod
    def get_teacher(self, first_name, last_name, email):
        pass
    @abstractmethod
    def change_teacher(self, first_name, last_name, email):
        pass
    @abstractmethod
    def remove_teacher(self, first_name, last_name, email):
        pass


class TeacherRepository(StudentRepositoryABC):
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=DB_CONFIG["dbname"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"],
        )

        self.cursor = self.conn.cursor()
        
    def check_teacher(self, first_name, last_name, email) -> bool:
        try:
            self.cursor.execute(
                "SELECT EXISTS (SELECT 1 FROM teachers WHERE first_name = %s AND last_name = %s AND email = %s)",
                (first_name, last_name, email,)
            )
            result = self.cursor.fetchone()[0]  # Fetch the boolean result
            return bool(result)  
        except psycopg2.Error as e:
            print(f"Ошибка проверки учителя: {e}")
            self.conn.rollback() 
            return False
        
    def add_teacher(self, first_name, last_name, email) -> bool:
        try:
            # Check if the teacher already exists
            if self.check_teacher(first_name, last_name, email):
                print(f"Учитель с именем {first_name}, фамилией {last_name} и email {email} уже существует.")
                return False  # Teacher already exists
            self.cursor.execute(
                "INSERT INTO teachers (first_name, last_name, email) VALUES (%s, %s, %s)", (first_name, last_name, email,))
            self.conn.commit()
            return True
        except psycopg2.Error as e:
            print(f"Ошибка добавления учителя: {e}")
            self.conn.rollback()
            return False

    def get_teacher(self, staff_id):
        try:
            self.cursor.execute("SELECT * FROM teachers WHERE  =%s", (staff_id,))
            return True if self.cursor.fetchone() else False
        except psycopg2.Error as e:
            print(f"Ошибка получения студента: {e}")
            return None
        
    def change_teacher(self, staff_id, first_name, last_name, email) -> bool:
        try:
            # Check if the teacher already exists
            if self.check_teacher(first_name, last_name, email):
                print(f"Учитель с именем {first_name}, фамилией {last_name} и email {email} уже существует.")
                return False  # Teacher already exists
            self.cursor.execute(
                """
                UPDATE teachers
                SET first_name = %s, last_name = %s, email = %s
                WHERE = %s
                """,
                (first_name, last_name, email, staff_id,)
            )
            self.conn.commit()
            return True
        except psycopg2.Error as e:
            print(f"Ошибка изменения учителя: {e}")
            self.conn.rollback()
            return False
        

    def remove_teacher(self, first_name, last_name, email) -> bool:
        try:
            # Check if the teacher already exists
            if self.check_teacher(first_name, last_name, email):
                print(f"Учитель с именем {first_name}, фамилией {last_name} и email {email} уже существует.")
                return False  # Teacher already exists
            self.cursor.execute(
                "DELETE FROM teachers WHERE first_name = %s AND last_name = %s AND email = %s",
                (first_name, last_name, email,)
            )
            self.conn.commit()
            return True
        except psycopg2.Error as e:
            print(f"Ошибка удаления учителя: {e}")
            self.conn.rollback()
            return False
        
    def close(self):
        self.cursor.close()
        self.conn.close()