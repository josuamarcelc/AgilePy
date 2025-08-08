# AgilePy 🐍

**AgilePy** is a minimal, modular Python micro-framework focused on clean frontend rendering using Flask — inspired by the simplicity of Lumen (PHP), but built the Pythonic way.

🌐 Website: [https://agilepy.com](https://agilepy.com)

---

## ⚡ Features

* 🚀 Fast and lightweight
* 🧹 Module-based views (no controllers)
* 🎨 Jinja2 templating
* 📁 Static asset support
* ☁️ Easy to deploy with Gunicorn + Nginx
* 🔍 Simple folder structure

---

## 📁 Project Structure

```
agilepy/
├── views/
│   └── home.py
├── templates/
│   └── home.html
├── static/
│   └── style.css
├── routes.py
├── app.py
├── wsgi.py
├── requirements.txt
└── README.md
```

---

## 🚀 Quickstart

### 1. Install dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Run the app

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000)

---

## 🌐 Deployment (Gunicorn + Nginx)

Create `wsgi.py`:

```python
from app import app

if __name__ == "__main__":
    app.run()
```

Run using:

```bash
gunicorn --bind 0.0.0.0:8000 wsgi:app
```

---

## 📄 Example View (`views/home.py`)

```python
from flask import render_template

def index():
    return render_template("home.html", title="Welcome to AgilePy")
```

---

## 📄 License

MIT License — free to use, modify, and share.

---

## 🤝 Contribute

Pull requests and issues welcome.

Join us at [AgilePy.com](https://agilepy.com)
