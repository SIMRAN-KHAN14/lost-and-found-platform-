
# Lost & Found Platform — Prototype

This is a simple Lost & Found web app prototype for managing lost and found items on a campus, in an office, or in any local community.

## What it does

- Lets anyone report a lost item or a found item through easy online forms.
- Stores reports in a real-time database (Firebase Firestore).
- Uses Google’s Gemini AI to automatically compare new reports and suggest possible matches.
- Shows all lost and found items on organized pages for anyone to view.
- Provides contact details to help owners and finders connect directly.

## Tech Stack

- Backend: Python + FastAPI
- Templates: Jinja2 (HTML)
- Database: Firebase Firestore
- AI Matching: Google Gemini (Generative AI)
- Server: Uvicorn

## Folder structure

lost_and_found_prototype/
 ├── main.py
 ├── firebase_config.json   # <-- Add your own Firebase credentials here
 ├── requirements.txt
 ├── templates/
 │   ├── index.html
 │   ├── lost.html
 │   ├── found.html
 │   ├── results.html
 ├── static/

## How to run

1. Clone or unzip the project folder.

2. Install the required packages:
   pip install -r requirements.txt

3. Add your Firebase credentials as firebase_config.json in the project root.

4. Set your Gemini API key as an environment variable:
   export GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"
   (On Windows, use set instead of export.)

5. Start the FastAPI server:
   uvicorn main:app --reload

6. Open your browser and go to:
   http://127.0.0.1:8000

7. Use the forms to report lost or found items and view them in the listings pages.

## Notes

- This is a basic prototype to show the core idea.
- For production, you should add user authentication, input validation, and better security.
- You can expand it with search, images, email notifications, and more!

## Created for

Solving the everyday hassle of tracking and reconnecting lost and found items in local communities using smart, simple technology.
