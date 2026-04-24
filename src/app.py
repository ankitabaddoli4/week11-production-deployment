from flask import Flask
import logging

def create_app():
    app = Flask(__name__)

    # -----------------------------
    # CONFIG
    # -----------------------------
    app.config["JSON_SORT_KEYS"] = False
    app.config["DEBUG"] = True

    # -----------------------------
    # ROUTES
    # -----------------------------
    @app.route("/")
    def home():
        return {"message": "Hello World"}

    # -----------------------------
    # LOGGING
    # -----------------------------
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return app


# Run only when executing directly
if __name__ == "__main__":
    app = create_app()
    print("🔥 Starting Flask Server...")
    app.run(host="0.0.0.0", port=5000, debug=True)
    