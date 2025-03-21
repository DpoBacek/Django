
### 1. Клонирование репозитория
Клонируйте репозиторий с GitHub:

git clone https://github.com/DpoBacek/Django.git
cd Django

### 2. Создание виртуальной среды
Создайте виртуальную среду для изоляции зависимостей проекта:

python -m venv env

### 3. Активация виртуальной среды
Активируйте виртуальную среду:

env\Scripts\activate

### 4. Установка зависимостей
Установите все зависимости, указанные в файле requirements.txt:

pip install -r requirements.txt

### 5. Настройка переменных окружения
Создайте файл .env в корне проекта и добавьте туда необходимые переменные окружения. Пример файла .env:

SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3

### 6. Применение миграций
Примените миграции для настройки базы данных:

python manage.py migrate

### 7. Создание суперпользователя (опционально)
Если вам нужен доступ к админке Django, создайте суперпользователя:

python manage.py createsuperuser

### 8. Запуск сервера разработки
Запустите сервер разработки Django:

