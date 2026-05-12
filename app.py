from flask import Flask
from routes import register_routes
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

base_app = Flask(__name__, template_folder="templates", static_folder="static")
register_routes(base_app)

# Mount under /dev
application = DispatcherMiddleware(Flask("root"), {
    "/dev": base_app
})

if __name__ == "__main__":
    run_simple("0.0.0.0", 5000, application, use_reloader=True)
