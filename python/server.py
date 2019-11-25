from absl import flags
from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)
    with app.app_context():
        return app


FLAGS = flags.FLAGS

app = create_app()

if __name__ == '__main__':
    app.run(debug=False, threaded=True)
