# HalalPin Backend Setup Instructions

## 1. Prerequisites
- Windows WSL2 or Ubuntu 22.04+
- Docker Desktop
- Python 3.11+
- PostgreSQL + PostGIS (for Docker only)

## 2. Clone Repo
```bash
git clone https://github.com/mellarch-technologies/halalpin-backend.git
cd halalpin-backend
```

## 3. Setup Environment Variables
Copy `.env.example` to `.env` and set variables:
```bash
cp .env.example .env
nano .env
# Set DJANGO_SECRET_KEY, etc
```

## 4. Run with Docker Compose
```bash
docker-compose up --build
```
- App at http://localhost:8000
- API at http://localhost:8000/api/
- Django admin at http://localhost:8000/admin

## 5. Run Initial Migrations
```bash
docker-compose exec backend python manage.py migrate
```

## 6. Create Superuser
```bash
docker-compose exec backend python manage.py createsuperuser
# Follow prompts for username/email/password
```

## 7. Create Initial Cities (via Admin)
1. Access http://localhost:8000/admin/
2. Log in with superuser credentials
3. Add Hyderabad, Lucknow, Chennai as cities (with population stats)

## 8. Development Workflow
- Edit code in WSL/Linux
- Restart Docker on code changes if needed

#### Issues?
- PostGIS error? See Docker logs for details.
- WSL2 networking: Use `localhost`, not 127.0.0.1 sometimes.

---

Questions? Raise GitHub Issues or ping project lead.

