Google Docs - https://docs.google.com/document/d/1jny8N5S4Npfvz9mCveuMjOehm7nQWT9tmpNaGn95n7Y/edit?tab=t.0

---------------------------------------------------------------------------------------------------------------------------------------------------------------

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

## 🔐 How to Create a Hugging Face API Key for Phi-3 Access

To use the **Phi-3** model or any other hosted model on Hugging Face via API, you need to generate an API key. Follow these steps:

### 📌 Step-by-Step Instructions

#### 1. Sign in or Sign up
- Visit [https://huggingface.co](https://huggingface.co)
- Log in to your account, or create one if you don’t already have it.

#### 2. Navigate to Access Tokens
- Click on your profile picture in the top-right corner.
- Select **"Settings"** from the dropdown menu.
- From the left sidebar, click on **"Access Tokens**" or go directly to:  
  [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

#### 3. Generate a New Token
- Click **"New token"**
- Enter a name (e.g., `phi3-token`)
- Choose a role:
  - Select **"Read"** if you only need to access and use models.
  - For most use cases, **"Read" is sufficient**.
- Click **"Generate"**

#### 4. Copy and Save the Token
- Copy the token shown — **you won’t be able to see it again**.
- Store it securely (e.g., in an environment variable or a secret manager).
- ⚠️ **Do NOT commit this token to version control (e.g., GitHub).**

---


## ❓ Troubleshooting

- If `python` or `pip` does not work on macOS/Linux, try `python3` and `pip3`.
- Always activate the virtual environment before running commands.
- Use `deactivate` to exit the virtual environment.

---

## 👨‍💻 Author

**Abhishek Patwardhan**  
GitHub: [https://github.com/AbhiMP2804](https://github.com/AbhiMP2804)

**Yash Joshi**  
GitHub: [GitHub](https://github.com/ypjoshi18)

---


