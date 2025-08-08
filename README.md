# AgilePy 🐍

**AgilePy** is a lightweight, modular Python micro-framework designed for building frontend-focused web apps with clean code and fast development. Inspired by the simplicity of Lumen (PHP), AgilePy lets you focus on views and routing, not boilerplate.

🌐 Website: [https://agilepy.com](https://agilepy.com)

---

## ✨ Why AgilePy?

* ✅ **Minimal**: No bloated tools or dependencies.
* 💡 **Modular**: Organize your views the way you like, using Python modules.
* 🎨 **Beautiful Templating**: Powered by Jinja2 (included in Flask).
* 🔧 **Zero config**: Just clone and run.
* 🚀 **Deploy-ready**: Works with Gunicorn + Nginx out of the box.

---

## 📁 Clean Project Structure

```
agilepy/
├── views/              # Python view modules
│   └── home.py        # Example view module
├── templates/          # HTML files with Jinja2 templating
│   └── home.html
├── static/             # CSS, JS, assets
│   └── style.css
├── routes.py           # Route definitions
├── app.py              # Main entry point
├── wsgi.py             # Deployment entry for Gunicorn
├── requirements.txt    # Required packages
└── README.md
```

---

## 🚀 Quickstart

### 1. Install Requirements

```bash
apt install python3-venv
apt install python3.10-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Run the App (Dev Mode)

```bash
python app.py
```

Open your browser at: [http://localhost:5000](http://localhost:5000)

---

## 🌐 Deployment Guide (Gunicorn + Nginx)

### Create `wsgi.py`

```python
from app import app

if __name__ == "__main__":
    app.run()
```

### Run via Gunicorn

```bash
gunicorn --bind 0.0.0.0:8000 wsgi:app
```

> For production setup with Nginx + SSL, see the docs at [AgilePy.com](https://agilepy.com)

---

## 🖊️ Sample View Module: `views/home.py`

```python
from flask import render_template

def index():
    return render_template("home.html", title="Welcome to AgilePy")
```

---

## 📚 License

AgilePy is open-source under the **MIT License** — free to use, modify, and distribute.

---

## 👍 Contributing

We welcome contributions of all kinds!

* Report bugs
* Suggest features
* Submit pull requests

Join the AgilePy community at [AgilePy.com](https://agilepy.com)
