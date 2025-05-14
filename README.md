Install django - pip install django


copy this project and run the project using python manage.py runserver ( be sure to be in right directory)


Google Docs - https://docs.google.com/document/d/1jny8N5S4Npfvz9mCveuMjOehm7nQWT9tmpNaGn95n7Y/edit?tab=t.0



Code Running Instructions after Installing Django:

1) Clone the repo : git clone https://github.com/ypjoshi18/adaptive_learning_webapp.git
2) Open New Terminal of your Idea or Editor
3) Move into adaptive learning directory by : cd adaptive_Learning
4) again repeat step 3
5) run 'ls' command and you should see the manage.py file
6) Run the Command : python manage.py runserver
7) Click on the link to view the web site 

# 🎬 Django Web Application

This is a Django-based web application. This guide will walk you through setting it up from scratch, including Python installation, environment setup, and running the server.

---

## 📦 Prerequisites

- Python 3.11 or higher
- pip (Python package installer)
- Git (optional, for cloning)
- Basic terminal/command-line usage

---

## 🧰 Step-by-Step Setup

### 1️⃣ Install Python & pip

Download and install Python from the official website:

🔗 https://www.python.org/downloads/

> ✅ During installation, ensure you check **"Add Python to PATH"**.

To verify installation:

```bash
python --version
pip --version
```

---

### 2️⃣ Clone the Project Repository

Clone this repository or download the ZIP.

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

Or download the ZIP and extract it manually.

---

### 3️⃣ Create & Activate Virtual Environment

Create a virtual environment (recommended):

```bash
python -m venv venv
```

Activate it:

- **Windows**:
  ```bash
  .\venv\Scripts\activate
  ```

- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

---

### 4️⃣ Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

> If you don't have a `requirements.txt` yet, you can create one by running:
>
> ```bash
> pip freeze > requirements.txt
> ```

---

### 5️⃣ Apply Migrations

Run database migrations to set up the initial schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6️⃣ Create a Superuser (Admin Access)

Create an admin account to access the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to set a username, email, and password.

---

### 7️⃣ Run the Server

Start the development server:

```bash
python manage.py runserver
```

Visit the site in your browser:

- App: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Admin Panel: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 📂 Project Structure (Sample)

```
your-username/your-repo-name/
├── manage.py
├── requirements.txt
├── README.md
├── db.sqlite3
├── your_project/
│   ├── settings.py
│   └── ...
├── your_app/
│   ├── views.py
│   ├── models.py
│   └── ...
```

---

## 📄 Sample `requirements.txt`

Here’s what a minimal `requirements.txt` might look like:

```txt
Django>=3.2
numpy
pandas
```

You can regenerate this file from your virtual environment anytime:

```bash
pip freeze > requirements.txt
```

---

## ❓ Troubleshooting

- Use `python3` instead of `python` if needed (Linux/macOS).
- Ensure you activate your virtual environment before installing or running.
- Use `pip3` if `pip` does not work.

---

## 👨‍💻 Author

**Your Name**  
GitHub: [https://github.com/your-username](https://github.com/your-username)

---

## 📜 License

This project is licensed under the MIT License.
