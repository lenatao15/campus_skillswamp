import os
import django
import random

# Настройка окружения Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'campus_skillSwamp.settings')
django.setup()

from django.contrib.auth.models import User
from skills.models import Category, Skill, Review

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
        ('diana', 'diana@example.com', 'pass12345'),
    ]
    users = []
    for username, email, password in users_data:
        user, created = User.objects.get_or_create(username=username, email=email)
        if created:
            user.set_password(password)
            user.save()
            print(f"User '{username}' created.")
        users.append(user)

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
    ]

    # 4. Добавляем навыки и отзывы
    comments = [
        "Amazing experience, highly recommended!",
        "Very helpful and professional.",
        "Great value for money.",
        "Exactly what I was looking for.",
        "Good, but could be better organized.",
        "Excellent teacher, very patient.",
        "Really enjoyed the session!",
    ]

    for s in skills_to_add:
        skill, created = Skill.objects.get_or_create(
            title=s['title'],
            owner=s['owner'],
            defaults={
                'description': s['description'],
                'category': s['category'],
                'price': s['price'],
                'is_free': s['is_free'],
            }
        )
        print(f"Skill '{skill.title}' ready.")

        # Добавляем 1-3 случайных отзыва для каждого навыка
        if skill.reviews.count() == 0:
            potential_reviewers = [u for u in users if u != skill.owner]
            num_reviews = random.randint(1, 3)
            reviewers = random.sample(potential_reviewers, min(num_reviews, len(potential_reviewers)))
            
            for reviewer in reviewers:
                Review.objects.create(
                    skill=skill,
                    reviewer=reviewer,
                    rating=random.randint(4, 5), # Делаем отзывы позитивными для красоты
                    comment=random.choice(comments)
                )
                print(f"  - Added review from {reviewer.username}")

    print("Database populated with skills and reviews successfully!")

if __name__ == '__main__':
    populate()
