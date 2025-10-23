<h1 align="center">🖼️ Image Gallery API</h1>

<p align="center">
  <b>REST API для загрузки и просмотра изображений с интеграцией с Cloudinary</b><br>
  Выполнен по техническому заданию для стажёров Python/Django.
</p>

---

## 🎯 Цель проекта
Создать REST API для загрузки изображений в облако (Cloudinary)  
и хранения информации о них в базе данных.  
Цель — проверить знание Django REST Framework, сериализации, обработки медиафайлов и интеграции со сторонними API.

---

## ⚙️ Используемые технологии

| Технология | Назначение |
|-------------|-------------|
| 🐍 **Python 3.x** | Язык программирования |
| 🧱 **Django** | Веб-фреймворк |
| 🌐 **Django REST Framework** | Создание REST API |
| 🗄️ **PostgreSQL** | База данных |
| ☁️ **Cloudinary** | Хранение изображений |
| 🧩 **python-decouple** | Работа с `.env` |
| 🖼️ **Pillow** | Работа с изображениями |

---

## 📦 Установка и запуск

### 🔹 1. Клонирование репозитория
```bash
git clone <ссылка-на-репозиторий>
cd image_gallery
🔹 2. Создание виртуального окружения
bash
Copy code
python -m venv venv
source venv/bin/activate 
🔹 3. Установка зависимостей
bash
Copy code
pip install -r requirements.txt
🔹 4. Создание файла .env в корне проекта
bash
Copy code
SECRET_KEY=dev-secret-key-change-me

DB_NAME=image_gallery_db
DB_USER=hello
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

# Cloudinary credentials (из Dashboard)
CLOUDINARY_URL=cloudinary://API_KEY:API_SECRET@CLOUD_NAME
🔹 5. Применение миграций
bash
Copy code
python manage.py makemigrations
python manage.py migrate
🔹 6. Запуск сервера
bash
Copy code
python manage.py runserver
🧭 API Эндпоинты
Метод	URL	Описание
POST	/api/images/	Загрузить изображение
GET	/api/images/	Получить список изображений
GET	/api/images/<id>/	Получить одно изображение
DELETE	/api/images/<id>/	Удалить изображение

🧪 Примеры запросов
🔸 POST — загрузка изображения
bash
Copy code
curl -X POST http://127.0.0.1:8000/api/images/ \
  -F "title=Мой ролл" \
  -F "description=Вкусный и свежий" \
  -F "image=@/полный/путь/к/файлу.jpg"
Ответ:

json
Copy code
{
  "id": 1,
  "title": "Мой ролл",
  "description": "Вкусный и свежий",
  "image_url": "https://res.cloudinary.com/<cloud_name>/image/upload/v1730000000/image_gallery/файл.jpg",
  "cloudinary_public_id": "image_gallery/файл",
  "uploaded_at": "2025-10-23T12:34:56Z"
}
🔸 GET — список изображений
bash
Copy code
curl -X GET http://127.0.0.1:8000/api/images/
🔸 GET — одно изображение
bash
Copy code
curl -X GET http://127.0.0.1:8000/api/images/1/
🧰 Структура проекта
arduino
Copy code
image_gallery_project/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── images/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── services.py
│
├── manage.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
✅ Выполненные пункты ТЗ
 Настроен Django + DRF

 Создана модель ImageItem

 Сериализатор принимает ImageField

 Интеграция с Cloudinary

 ViewSet реализует POST, GET list, GET detail

 Логика загрузки вынесена в отдельный сервис

 Примеры curl-запросов добавлены

 Настроен README.md

🧑‍💻 Автор проекта
Стажёр Python/Django — Айпери
📅 Дата выполнения: Октябрь 2025
💬 Проект выполнен в рамках учебного ТЗ для стажировки.

<p align="center">💙 Спасибо за просмотр проекта 💙</p> ```