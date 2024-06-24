# worker.py
from celery_config import app

if __name__ == '__main__':
    argv = [
        'worker',
        '--loglevel=info',
        '-P', 'solo',
    ]
    app.worker_main(argv)