from typing import Any

from absl import flags
from elasticsearch import Elasticsearch
from flask import Flask, jsonify, request

client = Elasticsearch()


def create_app() -> Flask:
    app = Flask(__name__)
    with app.app_context():
        return app


FLAGS = flags.FLAGS

app = create_app()


@app.route('/elastic', methods=['GET'])
def query_elastic() -> Any:
    data = request.get_json()
    args = request.args
    result = client.search(index=args['index'], body=data)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=False, threaded=True)
