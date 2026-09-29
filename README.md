# FitBuddy: AI Fitness Plan Generator using Gemini

FitBuddy generates personalized 3-day workout plans and nutrition tips using Google Gemini. The workout plan streams live in the browser for instant feedback. Users can update plans via feedback, and an admin dashboard shows all users.

## Features

- Real-time streaming 3-day workout plan
- Nutrition and recovery tip based on your goal
- Feedback loop to update plans
- SQLite storage of users and plans
- Admin dashboard at /view-all-users

## Tech Stack

- FastAPI, Python, SQLAlchemy
- SQLite database
- Google Gemini (gemini-3.8-flash)
- HTML, CSS, Jinja2

## How to Run Locally

### 1. Clone the repository

    git clone https://github.com/luci/FitBuddy.git
    cd FitBuddy

### 2. Create and activate a virtual environment

    python -m venv venv
    venv\Scripts\activate

### 3. Install dependencies

    python -m pip install -r requirements.txt

### 4. Create a .env file

Add your Google Gemini API key to a file named `.env` in the project root:

    GOOGLE_API_KEY=AIzaSyYourActualKeyHere

### 5. Run the server

    python -m uvicorn app.main:app --reload

### 6. Open in your browser

    http://127.0.0.1:8000

## Project Structure

    FitBuddy/
    ├── app/
    │   ├── __init__.py
    │   ├── main.py
    │   ├── database.py
    │   ├── gemini_generator.py
    │   └── gemini_flash_generator.py
    ├── templates/
    │   ├── index.html
    │   ├── result.html
    │   └── all_users.html
    ├── static/
    │   └── style.css
    ├── .env
    ├── .gitignore
    ├── requirements.txt
    └── README.md