from flask import Flask
from app.routes import main

app = Flask(__name__)

# Register blueprints
app.register_blueprint(main)

# Error handling (optional)
@app.errorhandler(404)
def not_found(error):
return "Page not found", 404

if __name__ == "__main__":
app.run(port=5001)
