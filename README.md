GitHub Webhook Receiver with Flask, MongoDB & Docker 

This project captures GitHub events (push, pull_request, merge) via webhooks, stores them in MongoDB, and displays them in real-time using a minimal UI. Built using Flask, MongoDB, and JavaScript.

---

Features

- GitHub webhook receiver for push, pull_request, and merge events
- Stores structured event data in MongoDB
- Minimal frontend that polls new events every 15 seconds
- Docker-free setup

---

Project Structure

.
├── app/
│   ├── extensions.py        # MongoDB setup
│   ├── __init__.py          # Flask app factory
│   └── webhook/
│       ├── routes.py        # Webhook receiver logic
│       ├── ui.py            # UI routes
│       └── utils.py         # Date formatting utility
├── templates/
│   └── index.html           # UI template
├── static/
│   └── js/
│       └── index.js         # Polls new events every 15 seconds
├── run.py
├── requirements.txt
└── README.txt

---

Getting Started
### ✅ Prerequisites

- Docker & Docker Compose
- GitHub account

### 🔧 Clone the Repos

```bash
git clone https://github.com/YOUR_USERNAME/webhook-repo.git
cd webhook-repo
docker-compose up --build
```
 #OR

1. Install Requirements
### 🔧 Clone the Repos

```bash
git clone https://github.com/YOUR_USERNAME/webhook-repo.git

cd webhook-repo
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```
2. Run MongoDB locally (default URI: mongodb://localhost:27017)

3. Start Flask App

python run.py

Visit:
- UI: http://localhost:5000/get_data/
- Webhook: http://localhost:5000/webhook/receiver

---

Setting Up GitHub Webhook

1. Go to your GitHub repo (action-repo)
2. Click on Settings → Webhooks → Add webhook
3. Use:
   - Download and install ngrok
   - run command - ngrok Http 5000  
   - Payload URL: http://<ngrok-ip>:5000/webhook/receiver on github
   - Content type: application/json
   - Events: push, pull_request
4. Click Add webhook

---



Frontend UI

- Located at /get_data/
- Polls the backend every 15 seconds
- Only shows new events that haven't already been displayed

---

Technologies Used

- Python 3.9
- Flask
- MongoDB
- JavaScript (vanilla)

---

Author

Sathwik Devadiga
https://www.linkedin.com/in/sathwik-devadiga

---

License

This project is part of a developer assessment and is provided for educational and demonstration purposes.
