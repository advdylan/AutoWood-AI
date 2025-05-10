# AutoWood

**AutoWood** is a full-stack web application designed to optimize and manage woodcutting projects, production processes, and warehouse inventory. Built with a Django REST API backend and a Vue.js frontend, it offers features like cut optimization, project and order tracking, barcode/EAN generation, and custom PDF generation for technical documentation.

This project was created to showcase full-stack development skills and is ready to be deployed or expanded for use in real workshop or manufacturing environments.

---

## ⚙️ Backend – Django Setup

### Prerequisites
- Python 3.10+
- `pip` and `venv`
- SQLite (default DB)

### Step-by-Step Setup

```bash
# 1. Navigate to the backend directory
cd backend

# 2. (Optional) Create and activate a virtual environment in the project root
python -m venv ../venv
source ../venv/bin/activate  # On Windows: ../venv/Scripts/activate

# 3. Install required packages
pip install -r ../requirements.txt

# 4. Run database migrations
python manage.py migrate

# 5. (Optional) Load initial data (if provided)
python manage.py loaddata initial_json.json

# 6. Start the development server
python manage.py runserver


🌐 Frontend – Vue.js Setup

Prerequisites

Node.js (v16+ recommended)

npm 

# 1. Navigate to the frontend directory
cd frontend

# 2. Install frontend dependencies
npm install

# 3. Run the Vue development server
npm run serve