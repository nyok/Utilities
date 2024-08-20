from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException



def take_screenshot(url, save_path, full_page=False, window_size=(1920, 1080)):
    options = Options()
    options.add_argument("--headless")

    service = Service('./chromedriver')
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.set_window_size(*window_size)
        driver.get(url)

        if full_page:
            total_height = driver.execute_script("return document.body.scrollHeight")
            driver.set_window_size(window_size[0], total_height)
            # Прокрутка до конца страницы
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.END)
            # Ждем пока страница загрузится полностью
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'html')))
        

        driver.save_screenshot(save_path)
        print(f"Скриншот сохранен: {save_path}")

    except TimeoutException:
        print("Время ожидания истекло. Страница не загружена полностью.")

    except Exception as e:
        print(f"Ошибка при создании скриншота: {e}")
    
    finally:
        driver.quit()

# Пример использования:
urls = [
    {"url": "https://google.com", "save_path": "example.png", "full_page": True},
    # ...
]

for page in urls:
    take_screenshot(**page)