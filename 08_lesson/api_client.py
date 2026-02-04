import requests
from typing import Optional, Dict, Any


class YougileAPIClient:
    """Клиент для работы с API Yougile."""
    
    def __init__(self, base_url: str, auth_headers: Dict[str, str]):
        """
        Инициализация клиента.
        
        Args(аргументы):
            base_url: Базовый URL API
            auth_headers: Заголовки авторизации
        """
        self.base_url = base_url
        self.auth_headers = auth_headers
        
    def create_project(self, title: str, description: Optional[str] = None) -> requests.Response:
        """
        Создание нового проекта.
        
        Args(аргументы):
            title: Название проекта (обязательное поле)
            description: Описание проекта (опционально)
            
        Returns:
            Response объект от API
        """
        url = f"{self.base_url}/api-v2/projects"
        payload = {"title": title}
        
        if description:
            payload["description"] = description
            
        response = requests.post(
            url=url,
            json=payload,
            headers=self.auth_headers
        )
        return response
    
    def update_project(self, project_id: str, title: Optional[str] = None, 
                      description: Optional[str] = None) -> requests.Response:
        """
        Обновление существующего проекта.
        
        Args:
            project_id: ID проекта
            title: Новое название проекта (опционально)
            description: Новое описание проекта (опционально)
            
        Returns:
            Response объект от API
        """
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        payload = {}
        
        if title:
            payload["title"] = title
        if description:
            payload["description"] = description
            
        response = requests.put(
            url=url,
            json=payload,
            headers=self.auth_headers
        )
        return response
    
    def get_project(self, project_id: str) -> requests.Response:
        """
        Получение информации о проекте.
        
        Args:
            project_id: ID проекта
            
        Returns:
            Response объект от API
        """
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        
        response = requests.get(
            url=url,
            headers=self.auth_headers
        )
        return response