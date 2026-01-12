# 🎬 CineFlowX – Smart Cinema Booking Platform

CineFlowX is a **BookMyShow-inspired movie ticket booking web application** built with Django and Tailwind CSS.  
It provides a cinematic, premium user experience with real-world booking flow including movies, theatres, showtimes, seat selection, and scalable backend design.

---

## 🚀 Features

➡️ Dynamic movie listings with posters, genres & languages  
➡️ Theatre-wise show grouping with multiple show timings  
➡️ Interactive seat selection layout  
➡️ Premium cinematic UI using Tailwind CSS  
➡️ Admin-controlled data (movies, theatres, shows, seats)  
➡️ Scalable backend architecture (real-world ready)  
➡️ Designed to impress judges & recruiters  

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, Tailwind CSS
- **Database:** SQLite (can be upgraded to PostgreSQL)
- **Templating:** Django Templates
- **Styling:** Tailwind CDN
- **Version Control:** Git & GitHub

---

## 📂 Project Structure
bookmyshow_clone/ │ ├── core/                  # Main project settings & URLs ├── movies/                # Movies app (movies, genres, languages) │   ├── models.py │   ├── views.py │   ├── urls.py │   └── static/movies/posters/ │ ├── shows/                 # Theatre, screen, show & seat logic │   ├── models.py │   ├── views.py │   ├── urls.py │   └── management/ │       └── commands/ │           └── seed_shows.py │ ├── templates/ │   ├── base.html │   ├── movies/ │   └── shows/ │ ├── db.sqlite3 ├── manage.py └── README.md

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/cineflowx.git
cd cineflowx

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install django

4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Seed Sample Data (Movies, Theatres, Shows)
python manage.py seed_shows

6️⃣ Create Admin User
python manage.py createsuperuser

7️⃣ Run the Server
python manage.py runserver

➡️ Open browser: http://127.0.0.1:8000/
🔐 Admin Panel
Access admin dashboard here:
http://127.0.0.1:8000/admin/
