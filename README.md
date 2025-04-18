**# ARCHA CODING CHALLENGE**

**Coding Task:** Transaction Management API
**Objective:**
- Develop a small RESTful API using Django and Django REST Framework that allows users to create a ‘Transaction’ and retrieve a list of them.
- The API should include endpoints to create transactions & retrieve them.
- The solution should be delivered as either a link to a github repository, or as a
- zip file containing the git repo with full commit history.

## 🚀 Features

- ✅ REST API with Django
- 🔐 JWT Authentication
- 📦 Dockerized for development

## 🛠️ Installation

```bash
git clone https://github.com/vroselined/archa_cc.git
cd archa_cc
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

**📚 API**
Method | Endpoint | Description
POST | /transaction/ | Create a new transaction
GET | /transaction/<id>/ | Get transaction details

**🧪 Running Tests**
```bash
python manage.py test
```
