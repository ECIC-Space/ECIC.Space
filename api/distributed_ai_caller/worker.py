# worker.py
from celery_config import app

if __name__ == '__main__':
    app.worker_main(['worker', '--loglevel=info'])