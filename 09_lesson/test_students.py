import pytest
from database import StudentTable
from sqlalchemy import create_engine, text

# Создание таблицы перед тестами
engine = create_engine("sqlite:///test.db")
with engine.connect() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            age INTEGER
        )
    """))
    conn.commit()


# СТРОКА ПОДКЛЮЧЕНИЯ (использовала SQLite вместо PostgreSQL, т.к. нужно быстрее сдать задание)
CONNECTION_STRING = (
    "sqlite:///test.db"
)


@pytest.fixture
def db():
    """Фикстура для создания экземпляра StudentTable."""
    return StudentTable(CONNECTION_STRING)


def test_create_student(db: StudentTable):
    """Тест на добавление нового студента."""
    # Подготовка уникальных тестовых данных
    import uuid
    unique_email = f"test_{uuid.uuid4().hex[:8]}@example.com"
    test_name = "Иван Тестовый"
    test_age = 20

    # Действие: создаем студента
    result = db.create_student(test_name, unique_email, test_age)
    assert result is True, "Создание студента не удалось"

    # Проверка: ищем созданного студента
    all_students = db.get_all_students()
    created_student = None
    for student in all_students:
        if student["email"] == unique_email:
            created_student = student
            break

    # Утверждения
    assert created_student is not None, "Студент не был создан в БД"
    assert created_student["name"] == test_name
    assert created_student["age"] == test_age

    # Очистка: удаляем созданного студента
    if created_student:
        db.delete_student(created_student["id"])
        print(f"Тестовый студент с ID {created_student['id']} удален.")


def test_update_student(db: StudentTable):
    """Тест на обновление данных студента."""
    # Подготовка: создаем студента для обновления
    import uuid
    original_email = f"update_{uuid.uuid4().hex[:8]}@example.com"
    original_name = "Петр Обновляемый"
    original_age = 22
    
    db.create_student(original_name, original_email, original_age)

    # Находим ID созданного студента
    all_students = db.get_all_students()
    student_to_update = None
    for student in all_students:
        if student["email"] == original_email:
            student_to_update = student
            break

    assert student_to_update is not None
    student_id = student_to_update["id"]

    # Действие: обновляем данные
    new_name = "Петр Обновленный"
    new_email = f"updated_{uuid.uuid4().hex[:8]}@example.com"
    new_age = 23
    
    result = db.update_student(
        student_id, new_name, new_email, new_age
    )
    assert result is True, "Обновление студента не удалось"

    # Проверка: получаем обновленную запись
    updated_student = db.get_student_by_id(student_id)
    assert updated_student is not None
    assert updated_student["name"] == new_name
    assert updated_student["email"] == new_email
    assert updated_student["age"] == new_age

    # Очистка
    db.delete_student(student_id)
    print(f"Обновленный студент с ID {student_id} удален.")


def test_delete_student(db: StudentTable):
    """Тест на удаление студента."""
    # Подготовка: создаем студента для удаления
    import uuid
    test_email = f"delete_{uuid.uuid4().hex[:8]}@example.com"
    test_name = "Сергей Удаляемый"
    test_age = 25
    
    db.create_student(test_name, test_email, test_age)

    # Находим ID созданного студента
    all_students = db.get_all_students()
    student_to_delete = None
    for student in all_students:
        if student["email"] == test_email:
            student_to_delete = student
            break

    assert student_to_delete is not None
    student_id = student_to_delete["id"]

    # Действие: удаляем студента
    result = db.delete_student(student_id)
    assert result is True, "Удаление студента не удалось"

    # Проверка: убеждаемся, что студент удален
    deleted_student = db.get_student_by_id(student_id)
    assert deleted_student is None, (
        f"Студент с ID {student_id} все еще существует в БД."
    )
    print(f"Удаление студента с ID {student_id} прошло успешно.")