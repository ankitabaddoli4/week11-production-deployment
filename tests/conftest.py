import sys
import os
import pytest

# Fix import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True
    })
    return app
