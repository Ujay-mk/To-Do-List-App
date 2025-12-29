TaskFlow: A Persistent Flask To-Do App
TaskFlow is a clean, lightweight web application designed to help users manage daily tasks. Unlike basic tutorial apps, TaskFlow features a persistent storage system, meaning your tasks remain saved even after closing the browser or restarting the server.

🚀 Features
Create & Delete: Easily add new tasks or remove completed ones.

Data Persistence: Tasks are saved to a local task.json file automatically.

Modern UI: Styled with a clean, responsive CSS card layout.

Safe Deletion: Uses POST request methods to prevent accidental deletions from search engine crawlers or browser pre-fetching.

Custom 404 Page: A dedicated error handler for a smooth user experience.

🛠️ Tech Stack
Backend: Python 3.x, Flask

Frontend: HTML5, CSS3, Jinja2 (Templating Engine)

Storage: JSON (Flat-file database)

📦 Installation & Setup
Clone the repository:

Bash

git clone https://github.com/yourusername/taskflow.git
cd taskflow
Install Flask:

Bash

pip install flask
Run the application:

Bash

python app.py
Access the app: Open your browser and go to http://localhost:8080

📂 Project Structure
Plaintext

├── app.py            # Main Flask application logic
├── task.json         # Local data storage (created automatically)
├── static/
│   └── style.css     # App styling and layout
└── templates/
    ├── index.html    # Main dashboard
    └── pnf.html      # 404 Page Not Found
Pro-Tip for your Repository:
If you want to make it look even better, you can take a screenshot of your app and ad
