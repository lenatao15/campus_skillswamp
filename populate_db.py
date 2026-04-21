import os
import django
import random

# Настройка окружения Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'campus_skillSwamp.settings')
django.setup()

from django.contrib.auth.models import User
from skills.models import Category, Skill, Review, Booking

def populate():
    print("Starting extended population script...")

    # 1. Категории
    categories_data = ['Cooking', 'Crafting', 'Tech', 'Music', 'Languages', 'Fitness', 'Art', 'Academic']
    categories = {}
    for cat_name in categories_data:
        cat, created = Category.objects.get_or_create(name=cat_name)
        categories[cat_name] = cat

    # 2. Пользователи
    users_data = [
        ('alice', 'alice@example.com'),
        ('bob', 'bob@example.com'),
        ('charlie', 'charlie@example.com'),
        ('diana', 'diana@example.com'),
        ('eric', 'eric@example.com'),
        ('fiona', 'fiona@example.com'),
    ]
    users = []
    for username, email in users_data:
        user, created = User.objects.get_or_create(username=username, email=email)
        if created:
            user.set_password('pass12345')
            user.save()
        users.append(user)

    # 3. Расширенный список навыков
    extended_skills = [
        ('Japanese for Beginners', 'Learn Hiragana and basic phrases.', 'Languages', 15.00, False),
        ('UI/UX Design Basics', 'Introduction to Figma and design principles.', 'Tech', 30.00, False),
        ('Personal Training Session', 'One hour of high-intensity workout.', 'Fitness', 0.00, True),
        ('Watercolor Painting', 'Master the basics of watercolor techniques.', 'Art', 20.00, False),
        ('Calculus Tutoring', 'Help with limits, derivatives, and integrals.', 'Academic', 25.00, False),
        ('Electronic Music Production', 'Learn how to use Ableton Live.', 'Music', 40.00, False),
        ('Bread Baking 101', 'Make your own sourdough at home.', 'Cooking', 10.00, False),
        ('Pottery Wheel for Beginners', 'Learn to throw clay on the wheel.', 'Crafting', 35.00, False),
        ('JavaScript/React Help', 'Debug your web applications.', 'Tech', 0.00, True),
        ('Yoga for Stress Relief', 'Gentle flow to relax after classes.', 'Fitness', 5.00, False),
        ('Portrait Photography', 'Tips for lighting and composition.', 'Art', 15.00, False),
        ('Spanish Conversation', 'Practice speaking with a fluent speaker.', 'Languages', 12.00, False),
        ('Basic First Aid', 'Essential life-saving skills.', 'Academic', 0.00, True),
        ('Drumming Lessons', 'Learn basic rock beats and fills.', 'Music', 20.00, False),
        ('Vegan Meal Prep', 'Plan your healthy meals for the week.', 'Cooking', 10.00, False),
    ]

    comments = [
        "Amazing experience, highly recommended!", "Very helpful and professional.",
        "Great value for money.", "Exactly what I was looking for.",
        "Excellent teacher, very patient.", "Really enjoyed the session!",
        "Super clear explanations.", "Would definitely book again."
    ]

    booking_messages = [
        "Hi! I'd love to learn this. Are you free this weekend?",
        "I'm struggling with this topic, could you help me out?",
        "This looks great, I'd like to book a session.",
        "Hello, I am interested in your skill. When can we meet?",
        "Can we schedule a call for next Tuesday?"
    ]

    # 4. Создание данных
    for title, desc, cat_name, price, is_free in extended_skills:
        owner = random.choice(users)
        skill, created = Skill.objects.get_or_create(
            title=title,
            owner=owner,
            defaults={
                'description': desc,
                'category': categories[cat_name],
                'price': price,
                'is_free': is_free,
            }
        )
        print(f"Skill '{skill.title}' processed.")

        # Добавляем 2-4 отзыва
        potential_reviewers = [u for u in users if u != owner]
        num_reviews = random.randint(2, 4)
        for reviewer in random.sample(potential_reviewers, num_reviews):
            Review.objects.get_or_create(
                skill=skill,
                reviewer=reviewer,
                defaults={
                    'rating': random.randint(4, 5),
                    'comment': random.choice(comments)
                }
            )

        # Добавляем 1-2 запроса
        num_requests = random.randint(1, 2)
        for requester in random.sample(potential_reviewers, num_requests):
            Booking.objects.get_or_create(
                skill=skill,
                requester=requester,
                defaults={
                    'message': random.choice(booking_messages),
                    'status': random.choice(['pending', 'approved'])
                }
            )

    print(f"\nSuccessfully populated database with {len(extended_skills)} skills and corresponding data!")

if __name__ == '__main__':
    populate()
