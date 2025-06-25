#!/# server/testing/conftest.py

import pytest
from app import app, db

@pytest.fixture(scope='module', autouse=True)
def setup_database():
    with app.app_context():
        db.create_all()      # ✅ Create tables before tests
        yield
        db.session.remove()
        db.drop_all()        # 🔁 Optional: Clean up after tests
