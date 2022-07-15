# source: http://docs.gunicorn.org/en/stable/custom.html
import multiprocessing
from typing import Dict, Optional

import gunicorn.app.base
from flask import Flask
from twootfeed import create_app, param


class StandaloneApplication(gunicorn.app.base.BaseApplication):
    def __init__(
        self, current_app: Flask, options: Optional[Dict] = None
    ) -> None:
        self.options = options or {}
        self.application = current_app
        super().__init__()

    def load_config(self) -> None:
        config = {
            key: value
            for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self) -> Flask:
        return self.application


def number_of_workers() -> int:
    return (multiprocessing.cpu_count() * 2) + 1


def main() -> None:
    app = create_app()
    options = {
        'bind': f"{param['app']['host']}:{param['app']['port']}",
        'workers': param['app'].get('nb_workers', number_of_workers()),
    }
    StandaloneApplication(app, options).run()


if __name__ == '__main__':
    main()
