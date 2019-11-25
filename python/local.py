"""local.py runs the app's code without starting a server, not used in prod."""

from typing import Any

from absl import app, flags

FLAGS = flags.FLAGS


def main(_: Any) -> None:
    print('Hello world')
    return


if __name__ == '__main__':
    app.run(main)
