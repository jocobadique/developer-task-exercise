# 📘 Working Shifts Application — Developer Task Exercise

A full-stack application for managing **workers**, **shifts**, and **preferred timezone settings**.

Built with:

- **Backend:** Django REST Framework  
- **Database:** Google Cloud Firestore (Datastore Mode)  
- **Frontend:** Vue 3 + Vite + Tailwind  
- **Deployment:** Cloud Run (backend) + Firebase Hosting (frontend)

---

# 📂 Project Structure

```
developer-task-exercise/
│
├── backend-django/     # Django REST API
├── frontend-vue/       # Vue 3 frontend
└── README.md           # Main documentation
```

---

# ⚙️ Backend — Django (Google Cloud Datastore)

## 📌 Features
- IANA timezone storage (`GET/PUT /timezone`)
- Worker management (CRUD)
- Shift management (CRUD)
- Shift rules:
  - Prevent overlaps per worker  
  - Maximum shift length = **12 hours**
  - Store timestamps in **UTC**
  - Convert timestamps to preferred timezone on read
- Firestore (Datastore mode) as persistence store
- Works locally using Datastore Emulator
- Deployable to **Cloud Run**

---

# ▶️ Running the Backend Locally

### 1️⃣ Install dependencies

```bash
cd backend-django
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 2️⃣ Start Google Cloud Datastore Emulator

Terminal 1:

```bash
gcloud beta emulators datastore start --host-port=localhost:8081
```

Terminal 2:

```bash
export DATASTORE_EMULATOR_HOST=localhost:8081
export DATASTORE_PROJECT_ID=developer-task-exercise
```

---

### 3️⃣ Run Django server

```bash
python manage.py runserver
```

API URL:
```
http://127.0.0.1:8000/api/
```

---

# 🧪 Backend API Endpoints

### **Timezone**
| Method | Endpoint              | Description |
|--------|------------------------|-------------|
| GET    | `/api/timezone/`       | Get preferred timezone |
| PUT    | `/api/timezone/`       | Update preferred timezone |

---

### **Workers**
| Method | Endpoint                   | Description |
|--------|-----------------------------|-------------|
| GET    | `/api/workers/`             | List workers |
| POST   | `/api/workers/`             | Add worker |
| PUT    | `/api/workers/<id>/`        | Update worker |
| DELETE | `/api/workers/<id>/`        | Remove worker |

---

### **Shifts**
| Method | Endpoint                   | Description |
|--------|-----------------------------|-------------|
| GET    | `/api/shifts/`              | List shifts |
| POST   | `/api/shifts/`              | Create shift |
| GET    | `/api/shifts/<id>/`         | View a shift |
| PUT    | `/api/shifts/<id>/`         | Update shift |
| DELETE | `/api/shifts/<id>/`         | Delete shift |

---

# 🎨 Frontend — Vue 3 + Vite + Tailwind

## 📌 Features
- Worker management UI  
- Shift management UI  
- Searchable **Timezone selector**
- Searchable **Worker selector**
- Form validation  
- Toast notifications  
- Responsive layout  
- Axios-based API client  
- Environment-based API URL

---

# ▶️ Running the Frontend Locally

```bash
cd frontend-vue
npm install
npm run dev
```

Frontend will be available at:

```
http://localhost:5173/
```

---

# 🔧 Frontend Environment Variables

Create:

`frontend-vue/.env`

```
VITE_API_BASE_URL=http://127.0.0.1:8000/api
```

When backend goes live on Cloud Run:

```
VITE_API_BASE_URL=https://your-cloudrun-url/api
```

---

# 🚀 Deployment

## ☁️ Deploy Backend to Cloud Run

### 1️⃣ Build container

```bash
cd backend-django
gcloud builds submit --tag gcr.io/PROJECT-ID/shifts-api
```

### 2️⃣ Deploy to Cloud Run

```bash
gcloud run deploy shifts-api \
  --image gcr.io/PROJECT-ID/shifts-api \
  --platform managed \
  --allow-unauthenticated
```

### 3️⃣ Configure frontend `.env` with Cloud Run URL

```
VITE_API_BASE_URL=https://CLOUDRUN-URL/api
```

---

## 🔥 Deploy Frontend to Firebase Hosting

### 1️⃣ Build

```bash
cd frontend-vue
npm run build
```

### 2️⃣ Initialize Firebase

```bash
firebase init hosting
```

### 3️⃣ Deploy

```bash
firebase deploy
```

Hosting URL will be provided by Firebase.

---

# 🧪 Testing

### Backend tests (pytest)

```bash
pytest
```

### Frontend tests

```bash
npm run test
```


# 👨‍💻 Author  
**Joco Badique**  
Software Engineer  
Email: Joco Badique

