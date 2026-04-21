# Campus SkillSwamp

**Campus SkillSwamp** is a web platform designed for students and community members to exchange skills, knowledge, and services. Whether you want to teach coding, learn guitar, or find a tutor for mathematics, this platform facilitates the connection between mentors and learners.

## 🚀 Features

- **Skill Management**: Users can create, update, and manage their own skill listings.
- **Categorization**: Browse skills organized by specific categories.
- **Booking System**: Request a skill session with a personalized message and track the booking status (Pending, Approved, Rejected, Completed).
- **Review System**: Leave feedback and star ratings (1 to 5) for skills you have utilized.
- **User Dashboard**: A personalized space to manage your listings and track your requests.
- **Authentication**: Secure signup and login system.

## 🛠️ Tech Stack

- **Framework**: [Django 6.0](https://www.djangoproject.com/)
- **Language**: Python
- **Database**: SQLite (default)
- **Frontend**: Django Templates with Vanilla CSS

## 📋 Prerequisites

- Python 3.10+
- pip (Python package installer)

## 🔧 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/lenatao15/campus_skillswamp.git
   cd campus_skillswamp
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

5. **(Optional) Populate the database**:
   ```bash
   python populate_db.py
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   Open your browser and go to `http://127.0.0.1:8000/`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
