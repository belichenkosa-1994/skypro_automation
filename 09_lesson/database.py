from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError


class StudentTable:
    """Класс для работы с таблицей students в базе данных."""

    __scripts = {
        "select_all": text("SELECT * FROM students"),
        "insert_new": text(
            "INSERT INTO students (name, email, age) "
            "VALUES (:name, :email, :age)"
        ),
        "update_by_id": text(
            "UPDATE students "
            "SET name = :name, email = :email, age = :age "
            "WHERE id = :id"
        ),
        "delete_by_id": text("DELETE FROM students WHERE id = :id"),
        "select_by_id": text("SELECT * FROM students WHERE id = :id"),
    }

    def __init__(self, connection_string: str):
        self._engine = create_engine(connection_string, echo=False)

    def get_all_students(self):
        """Получить всех студентов."""
        try:
            with self._engine.connect() as conn:
                result = conn.execute(self.__scripts["select_all"])
                # В версии 2.0 используем mappings() для получения словарей
                rows = result.mappings().all()
                return rows
        except SQLAlchemyError as e:
            print(f"Ошибка при получении студентов: {e}")
            return []

    def create_student(self, name: str, email: str, age: int):
        """Добавить нового студента."""
        try:
            with self._engine.connect() as conn:
                with conn.begin():
                    conn.execute(
                        self.__scripts["insert_new"],
                        {"name": name, "email": email, "age": age}
                    )
                return True
        except SQLAlchemyError as e:
            print(f"Ошибка при создании студента: {e}")
            return False

    def update_student(
        self, student_id: int, name: str, email: str, age: int
    ):
        """Обновить данные студента по ID."""
        try:
            with self._engine.connect() as conn:
                with conn.begin():
                    conn.execute(
                        self.__scripts["update_by_id"],
                        {
                            "id": student_id,
                            "name": name,
                            "email": email,
                            "age": age,
                        },
                    )
                return True
        except SQLAlchemyError as e:
            print(f"Ошибка при обновлении студента: {e}")
            return False

    def delete_student(self, student_id: int):
        """Удалить студента по ID."""
        try:
            with self._engine.connect() as conn:
                with conn.begin():
                    conn.execute(
                        self.__scripts["delete_by_id"], {"id": student_id}
                    )
                return True
        except SQLAlchemyError as e:
            print(f"Ошибка при удалении студента: {e}")
            return False

    def get_student_by_id(self, student_id: int):
        """Найти студента по ID. Возвращает None, если не найден."""
        try:
            with self._engine.connect() as conn:
                result = conn.execute(
                    self.__scripts["select_by_id"], {"id": student_id}
                ).mappings().first()
                return result
        except SQLAlchemyError as e:
            print(f"Ошибка при поиске студента: {e}")
            return None