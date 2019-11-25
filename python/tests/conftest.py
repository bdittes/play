import pytest
from flask import Flask

from python.server import create_app


@pytest.fixture
def app() -> Flask:
    app: Flask = create_app()
    # app.config.from_pyfile('../tests/flask_test_cfg.py')
    return app
