# Django Todo Application

Это проект Django для управления задачами Todo, использующий PostgreSQL в качестве базы данных и Docker для контейнеризации.


## Установка

### Клонирование репозитория

```bash
https://github.com/LeonidPetrov145/todo.git
cd todo
docker-compose up --build

```
# Создать новый терминал
```bash
docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py createsuperuser
```
## С помощью созданого SuperUser поменяйте роль одного из user на администратора для тестирования API
