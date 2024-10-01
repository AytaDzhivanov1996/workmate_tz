# API Онлайн-выставки котят

Это приложение использует Django Rest Framework, контейнеризацию через Docker и PostgreSQL в качестве БД.

## Требования

Убедитесь, что у вас установлен Docker
- [Install Docker](https://docs.docker.com/get-docker/)
- [Install Docker Compose](https://docs.docker.com/compose/install/)

## Быстрый старт

### 1. Клонируйте репозиторий

```
git clone https://github.com/AytaDzhivanov1996/workmate_tz.git
cd wormate_tz
```

### 2. Создайте .env файл

```bash
POSTGRES_DB=django_db
POSTGRES_USER=django_user
POSTGRES_PASSWORD=django_password
POSTGRES_HOST=db
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1
#Не забудьте про DEBUG и SECRET_KEY
```
### 3. Создание и запуск контейнеров
```bash
docker compose up --build
```

### 4. Создание суперпользователя (для админки)
```bash
docker compose run web python manage.py createsuperuser
```

### 5. Документация
```
http://127.0.0.1:8000/swagger/
```

### 6. Остановка контейнеров и очистка данных
```bash
docker compose down -v
```

### Прочие команды
- Перезапуск контейнеров
```bash
docker compose up --build
```
- Изменение и применение миграций
```bash
docker compose run web python manage.py makemigrations
docker compose run web python manage.py migrate
```
- Просмотр логов
```bash
docker compose logs -f
```
- Запуск тестов
```bash
docker compose run web pytest
```
- Точка входа в приложение
```bash
docker compose run web python manage.py <command>
```
