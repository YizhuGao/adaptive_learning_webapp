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

<details>
<summary>Windows</summary>

```bash
python --version
pip --version
```
</details>

<details>
<summary>macOS/Linux</summary>

```bash
python3 --version
pip3 --version
```
</details>

---

### 2️⃣ Clone the Project Repository

Clone this repository or download the ZIP.

```bash
git clone https://github.com/ypjoshi18/adaptive_learning_webapp.git
cd your-repo-name
```

Or download the ZIP and extract it manually.

---

### 3️⃣ Create & Activate Virtual Environment

Create a virtual environment:

<details>
<summary>Windows</summary>

```bash
python -m venv venv
.\venv\Scripts\activate
```
</details>

<details>
<summary>macOS/Linux</summary>

```bash
python3 -m venv venv
source venv/bin/activate
```
</details>

---

### 4️⃣ Install Dependencies

Install all required Python packages:

<details>
<summary>Windows</summary>

```bash
pip install Django numpy pandas torch
pip install -r requirements.txt
```
</details>

<details>
<summary>macOS/Linux</summary>

```bash
pip3 install Django numpy pandas torch
pip3 install -r requirements.txt
```
</details>

> If you don't have a `requirements.txt` yet, you can create one:

```bash
pip freeze > requirements.txt
```

---

### 5️⃣ Apply Migrations

Run database migrations:

<details>
<summary>Windows</summary>

```bash
python manage.py makemigrations
python manage.py migrate
```
</details>

<details>
<summary>macOS/Linux</summary>

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
</details>

---

### 6️⃣ Create a Superuser (Admin Access)

<details>
<summary>Windows</summary>

```bash
python manage.py createsuperuser
```
</details>

<details>
<summary>macOS/Linux</summary>

```bash
python3 manage.py createsuperuser
```
</details>

---

### 7️⃣ Run the Server

<details>
<summary>Windows</summary>

```bash
python manage.py runserver
```
</details>

<details>
<summary>macOS/Linux</summary>

```bash
python3 manage.py runserver
```
</details>

Now open your browser and go to:

- App: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Admin Panel: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 📂 Project Structure (Sample)

```
your-repo-name/
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

```txt
Django>=3.2
numpy
pandas
```

Generate it any time:

<details>
<summary>Windows</summary>

```bash
pip freeze > requirements.txt
```
</details>

<details>
<summary>macOS/Linux</summary>

```bash
pip3 freeze > requirements.txt
```
</details>

---

## ❓ Troubleshooting

- If `python` or `pip` does not work on macOS/Linux, try `python3` and `pip3`.
- Always activate the virtual environment before running commands.
- Use `deactivate` to exit the virtual environment.

---

## 👨‍💻 Author

**Abhishek Patwardhan**  
GitHub: [https://github.com/AbhiMP2804](https://github.com/AbhiMP2804)

---


