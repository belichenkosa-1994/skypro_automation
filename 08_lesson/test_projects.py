import pytest
import requests
import os
import uuid
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

BASE_URL = "https://ru.yougile.com/api-v2"
API_KEY = os.getenv('YOUGILE_API_KEY')
COMPANY_ID = os.getenv('YOUGILE_COMPANY_ID')


class TestYougileProjects:
    """Тесты для Yougile API"""
    
    def setup_method(self):
        """Настройка перед каждым тестом"""
        self.headers = {
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json'
        }
    
    # ПОЗИТИВНЫЕ ТЕСТЫ
    
    @pytest.mark.positive
    def test_create_project_positive(self):
        """Позитивный тест: создание проекта с title"""
        # Arrange (подготовка)
        url = f"{BASE_URL}/projects"
        project_title = f"Тестовый проект {uuid.uuid4().hex[:8]}"
        payload = {"title": project_title}
        
        # Act (действие)
        response = requests.post(url, json=payload, headers=self.headers)
        
        # Assert (проверка)
        assert response.status_code == 201
        response_data = response.json()
        assert "id" in response_data
        print(f"✅ Проект создан с ID: {response_data['id']}")
        
        # Возвращаем ID для использования в других тестах
        return response_data['id']
    
    @pytest.mark.positive
    def test_get_project_positive(self):
        """Позитивный тест: получение информации о проекте"""
        # Сначала создаем проект
        project_id = self.test_create_project_positive()
        
        # Потом получаем его
        url = f"{BASE_URL}/projects/{project_id}"
        response = requests.get(url, headers=self.headers)
        
        assert response.status_code == 200
        project_data = response.json()
        assert project_data["id"] == project_id
        print(f"✅ Проект получен: {project_data.get('title', 'без названия')}")
    
    @pytest.mark.positive
    def test_update_project_positive(self):
        """Позитивный тест: обновление существующего проекта"""
        # Сначала создаем проект
        project_id = self.test_create_project_positive()
        
        # Обновляем его
        url = f"{BASE_URL}/projects/{project_id}"
        new_title = f"Обновленный проект {uuid.uuid4().hex[:8]}"
        payload = {"title": new_title}
        
        response = requests.put(url, json=payload, headers=self.headers)
        
        assert response.status_code == 200
        updated_data = response.json()
        print(f"✅ Проект обновлен. Новое название: {updated_data.get('title', 'нет в ответе')}")
    
    # НЕГАТИВНЫЕ ТЕСТЫ
    
    @pytest.mark.negative
    def test_create_project_negative_no_title(self):
        """Негативный тест: создание проекта без title"""
        url = f"{BASE_URL}/projects"
        payload = {}  # Нет обязательного поля title!
        
        response = requests.post(url, json=payload, headers=self.headers)
        
        # Ожидаем ошибку валидации (400 Bad Request)
        assert response.status_code == 400
        print(f"✅ Корректная ошибка при отсутствии title: {response.status_code}")
    
    @pytest.mark.negative
    def test_get_project_negative_not_found(self):
        """Негативный тест: получение несуществующего проекта"""
        # Генерируем случайный UUID, которого точно нет
        fake_id = str(uuid.uuid4())
        url = f"{BASE_URL}/projects/{fake_id}"
        
        response = requests.get(url, headers=self.headers)
        
        # Ожидаем 404 Not Found
        assert response.status_code == 404
        print(f"✅ Корректная ошибка при запросе несуществующего проекта: {response.status_code}")
    
    @pytest.mark.negative
    def test_update_project_negative_not_found(self):
        """Негативный тест: обновление несуществующего проекта"""
        fake_id = str(uuid.uuid4())
        url = f"{BASE_URL}/projects/{fake_id}"
        payload = {"title": "Новое название"}
        
        response = requests.put(url, json=payload, headers=self.headers)
        
        # Ожидаем 404 Not Found
        assert response.status_code == 404
        print(f"✅ Корректная ошибка при обновлении несуществующего проекта: {response.status_code}")