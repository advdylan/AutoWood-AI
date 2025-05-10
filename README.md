# AutoWood

**AutoWood** is a full-stack web application for managing woodcutting projects and production processes. It combines a Vue.js frontend with a Django REST API backend. This tool is designed to streamline manufacturing steps—from material optimization to production tracking and warehouse inventory—while also providing custom features like barcode generation and PDF output for technical documentation.

AutoWood was developed as a portfolio-quality project to showcase real-world software development skills, deployment readiness, and frontend-backend integration.

---

## 📁 Project Structure

/frontend → Vue 3 SPA (client)
/backend → Django REST API (server)
/media → Uploaded files (Django media)
/logs → Debug logs
/venv → Python virtual environment (not committed)
/README.md → Project documentation

yaml
Copy
Edit

---

## ⚙️ Backend – Django Setup

### Prerequisites
- Python 3.10+
- pip
- virtualenv or venv

### Setup Instructions

```bash
# 1. Navigate to the backend directory
cd backend

# 2. (Optional) Create a virtual environment in the project root
python -m venv ../venv

# 3. Activate the environment
source ../venv/bin/activate       # macOS/Linux
# OR
../venv/Scripts/activate          # Windows

# 4. Install the required packages
pip install -r ../requirements.txt

# 5. Run database migrations
python manage.py migrate

# 6. (Optional) Load initial data
python manage.py loaddata initial_json.json

# 7. Start the backend server
python manage.py runserver
After running, the Django backend will be live at:
http://127.0.0.1:8000/

🌐 Frontend – Vue.js Setup
Prerequisites
Node.js (v16+ recommended)

npm

Setup Instructions
bash
Copy
Edit
# 1. Navigate to the frontend directory
cd frontend

# 2. Install all dependencies
npm install

# 3. Start the development server
npm run serve
After starting, the Vue app will be running at:
http://localhost:8080/

Make sure your backend is running in parallel so the frontend can connect to the API.

✨ Features
🔪 Intelligent cut optimization engine for board-based materials

📄 PDF generation with project details and layout plans

🏷️ Barcode (EAN) generator for order tracking and scanning

📦 Warehouse and stock management

🔄 Real-time production process tracking

📁 Media handling for file uploads and project files

🧰 Tech Stack
Layer	Technology
Frontend	Vue 3, Composition API
Backend	Python, Django, DRF
Database	SQLite (default)
Deployment	Docker, Fly.io
Extras	Barcode generation, PDF scripts, custom admin logic

📸 Screenshots
(Coming soon – add screenshots or GIFs of your UI and PDF outputs here!)

🧪 Development Notes
To start the entire app locally:

bash
Copy
Edit
# Terminal tab 1 – Backend
cd backend
source ../venv/bin/activate
python manage.py runserver

# Terminal tab 2 – Frontend
cd frontend
npm run serve
You can also use startup.sh inside /backend to automate some of the setup.

📝 License
This project is open-source and available under the MIT License.

vbnet
Copy
Edit

---

Would you like me to include optional enhancements like:
- `.env` file usage
- Deployment section (e.g., Docker/Fly.io)
- API routes auto-generated from DRF?

Let me know what direction you want the README to evolve next.