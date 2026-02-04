import os
import sys
import time
import shutil
import tempfile
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def nuclear_kill():
    """ЯДЕРНОЕ УНИЧТОЖЕНИЕ всех Chrome процессов"""
    print("☢️  ЯДЕРНОЕ УНИЧТОЖЕНИЕ Chrome...")

    kill_commands = [
        # Обычное завершение
        "taskkill /f /im chrome.exe >nul 2>&1",
        "taskkill /f /im chromedriver.exe >nul 2>&1",

        # WMIC - более надежно
        "wmic process where \"name='chrome.exe'\" delete >nul 2>&1",
        "wmic process where \"name='chromedriver.exe'\" delete >nul 2>&1",

        # PowerShell
        "powershell \"Get-Process chrome -ErrorAction SilentlyContinue | Stop-Process -Force\"",
        "powershell \"Get-Process chromedriver -ErrorAction SilentlyContinue | Stop-Process -Force\"",
    ]

    for cmd in kill_commands:
        try:
            subprocess.run(cmd, shell=True, timeout=2)
        except:
            pass

    # Ждем
    time.sleep(5)

    # Проверяем
    result = subprocess.run(
        "tasklist | findstr /i chrome",
        shell=True,
        capture_output=True,
        text=True
    )

    if "chrome.exe" in result.stdout.lower():
        print("❌ Chrome всё ещё жив! Перезагрузите компьютер!")
        return False
    else:
        print("✅ Все процессы Chrome убиты")
        return True


def get_chrome_path():
    """Найти Chrome"""
    paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expanduser(r"~\AppData\Local\Google\Chrome\Application\chrome.exe"),
        r"C:\Users\Public\Desktop\Google Chrome.lnk"
    ]

    for path in paths:
        if os.path.exists(path):
            return path

    # Поиск в PATH
    try:
        chrome_path = subprocess.check_output(
            "where chrome",
            shell=True,
            text=True
        ).strip().split('\n')[0]
        if os.path.exists(chrome_path):
            return chrome_path
    except:
        pass

    return None


def main():
    print("=" * 60)
    print("ФИНАЛЬНОЕ ИСПРАВЛЕНИЕ SESSIONNOTCREATEDEXCEPTION")
    print("=" * 60)

    # 1. Убить Chrome
    if not nuclear_kill():
        print("\n⚠️  Нужна перезагрузка! Запустите после перезагрузки.")
        return

    # 2. Найти Chrome
    chrome_path = get_chrome_path()
    if not chrome_path:
        print("❌ Chrome не найден! Установите Chrome.")
        return

    print(f"✅ Chrome найден: {chrome_path}")

    # 3. Создать ВРЕМЕННУЮ папку для профиля
    temp_profile = tempfile.mkdtemp(prefix="chrome_test_")
    print(f"📁 Временный профиль: {temp_profile}")

    # 4. ОПЦИИ которые ТОЧНО РАБОТАЮТ на Windows
    chrome_options = Options()

    # КРИТИЧЕСКИ ВАЖНЫЕ:
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument(f"--user-data-dir={temp_profile}")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument("--remote-debugging-address=0.0.0.0")

    # Для стабильности:
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-features=VizDisplayCompositor")

    # Отключаем логи
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # Явно указываем путь к Chrome
    chrome_options.binary_location = chrome_path

    # 5. Пробуем запустить РАЗНЫМИ СПОСОБАМИ
    print("\n🚀 Пробуем запустить Chrome...")

    methods = [
        # Способ 1: Без service (самый простой)
        lambda: webdriver.Chrome(options=chrome_options),

        # Способ 2: С указанием пути к chromedriver
        lambda: webdriver.Chrome(
            executable_path=os.path.join(os.path.dirname(chrome_path), "chromedriver.exe"),
            options=chrome_options
        ) if os.path.exists(os.path.join(os.path.dirname(chrome_path), "chromedriver.exe")) else None,

        # Способ 3: Headless режим
        lambda: webdriver.Chrome(options=chrome_options.add_argument("--headless=new")),
    ]

    driver = None
    for i, method in enumerate(methods):
        print(f"\n🔧 Способ {i + 1}...")
        try:
            driver = method()
            if driver:
                print(f"✅ Способ {i + 1} РАБОТАЕТ!")
                break
        except Exception as e:
            print(f"❌ Способ {i + 1} не работает: {str(e)[:100]}")

    if not driver:
        print("\n💥 ВСЕ способы не работают!")
        print("\n🔧 ПОСЛЕДНИЙ ШАНС: Попробуйте Firefox")
        try:
            from selenium.webdriver import Firefox
            from selenium.webdriver.firefox.options import Options as FirefoxOptions

            ff_options = FirefoxOptions()
            driver = Firefox(options=ff_options)
            print("✅ Firefox работает! Используйте его для тестов.")
        except Exception as e:
            print(f"❌ И Firefox не работает: {e}")

        # Удаляем временную папку
        try:
            shutil.rmtree(temp_profile, ignore_errors=True)
        except:
            pass
        return

    # 6. Тест
    try:
        print("\n🌐 Открываем страницу...")
        driver.get("https://www.google.com")
        print(f"✅ УСПЕХ! Страница: {driver.title}")

        # Демонстрация работы
        driver.save_screenshot("success.png")
        print("📸 Скриншот сохранен: success.png")

        time.sleep(2)

    except Exception as e:
        print(f"❌ Ошибка при работе: {e}")

    finally:
        # 7. Закрыть
        if driver:
            driver.quit()
            print("✅ Chrome закрыт")

        # Удалить временную папку
        try:
            shutil.rmtree(temp_profile, ignore_errors=True)
            print("✅ Временная папка удалена")
        except:
            pass

    print("\n" + "=" * 60)
    print("🎉 ЕСЛИ ВЫ ВИДИТЕ ЭТО - CHROME ЗАПУСТИЛСЯ!")
    print("=" * 60)


if __name__ == "__main__":
    main()