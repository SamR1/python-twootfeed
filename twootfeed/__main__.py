# source: http://docs.gunicorn.org/en/stable/custom.html
from __future__ import unicode_literals

import multiprocessing

import gunicorn.app.base
from twootfeed import create_app, param


class StandaloneApplication(gunicorn.app.base.BaseApplication):
    def __init__(self, current_app, options=None):
        self.options = options or {}
        self.application = current_app
        super().__init__()

    def load_config(self):
        config = {
            key: value
            for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


def number_of_workers():
    return (multiprocessing.cpu_count() * 2) + 1


def main():
    app = create_app()
    options = {
        'bind': f"{param['app']['host']}:{param['app']['port']}",
        'workers': param['app'].get('nb_workers', number_of_workers()),
    }
    StandaloneApplication(app, options).run()


if __name__ == '__main__':
    main()
