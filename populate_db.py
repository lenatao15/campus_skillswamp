import os
import django
import random

# Настройка окружения Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'campus_skillSwamp.settings')
django.setup()

from django.contrib.auth.models import User
from skills.models import Category, Skill

def populate():
    print("Starting population script...")

    # 1. Создаем категории
    categories_data = ['Cooking', 'Crafting', 'Tech', 'Music', 'Languages', 'Fitness']
    categories = {}
    for cat_name in categories_data:
        cat, created = Category.objects.get_or_create(name=cat_name)
        categories[cat_name] = cat
        print(f"Category '{cat_name}' ready.")

    # 2. Создаем пользователей
    users_data = [
        ('alice', 'alice@example.com', 'pass12345'),
        ('bob', 'bob@example.com', 'pass12345'),
        ('charlie', 'charlie@example.com', 'pass12345'),
    ]
    users = []
    for username, email, password in users_data:
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username, email, password)
            users.append(user)
            print(f"User '{username}' created.")
        else:
            users.append(User.objects.get(username=username))

    # 3. Список навыков для добавления
    skills_to_add = [
        {
            'title': 'Italian Pasta Masterclass',
            'description': 'Learn how to make authentic carbonara and fettuccine from scratch. Ingredients included!',
            'category': categories['Cooking'],
            'price': 25.00,
            'is_free': False,
            'owner': users[0], # Alice
        },
        {
            'title': 'Custom Hand-knit Sweaters',
            'description': 'I will knit a custom sweater for you. You choose the color and pattern. Takes about 2 weeks.',
            'category': categories['Crafting'],
            'price': 45.00,
            'is_free': False,
            'owner': users[1], # Bob
        },
        {
            'title': 'Python Debugging Help',
            'description': 'Struggling with your homework? I can help you find those pesky bugs in your Python code.',
            'category': categories['Tech'],
            'price': 0.00,
            'is_free': True,
            'owner': users[2], # Charlie
        },
        {
            'title': 'Beginner Guitar Lessons',
            'description': 'Want to play your favorite songs? I teach basic chords and strumming patterns.',
            'category': categories['Music'],
            'price': 15.00,
            'is_free': False,
            'owner': users[0], # Alice
        },
        {
            'title': 'French Conversation Practice',
            'description': 'Native speaker available for 1-on-1 conversation practice. Improve your fluency!',
            'category': categories['Languages'],
            'price': 10.00,
            'is_free': False,
            'owner': users[1], # Bob
        },
        {
            'title': 'Homemade Vegan Desserts',
            'description': 'Delicious brownies and cookies that are 100% vegan. Healthy and tasty!',
            'category': categories['Cooking'],
            'price': 5.00,
            'is_free': False,
            'owner': users[2], # Charlie
        },
        {
            'title': 'Diy Pottery Workshop',
            'description': 'Learn the basics of hand-building pottery. We will make mugs and bowls.',
            'category': categories['Crafting'],
            'price': 30.00,
            'is_free': False,
            'owner': users[0], # Alice
        },
        {
            'title': 'Excel for Business',
            'description': 'Master VLOOKUP, Pivot Tables, and data visualization for your next internship.',
            'category': categories['Tech'],
            'price': 20.00,
            'is_free': False,
            'owner': users[1], # Bob
        },
        {
            'title': 'Morning Yoga Sessions',
            'description': 'Start your day with energy. 45-minute yoga flow on the campus lawn.',
            'category': categories['Fitness'],
            'price': 0.00,
            'is_free': True,
            'owner': users[2], # Charlie
        },
        {
            'title': 'Basic Woodworking',
            'description': 'Learn how to use basic tools to build simple birdhouses or shelves.',
            'category': categories['Crafting'],
            'price': 20.00,
            'is_free': False,
            'owner': users[0], # Alice
        },
    ]

    # 4. Добавляем навыки в базу
    for s in skills_to_add:
        Skill.objects.get_or_create(
            title=s['title'],
            description=s['description'],
            category=s['category'],
            price=s['price'],
            is_free=s['is_free'],
            owner=s['owner']
        )
        print(f"Skill '{s['title']}' added.")

    print("Database populated successfully!")

if __name__ == '__main__':
    populate()
