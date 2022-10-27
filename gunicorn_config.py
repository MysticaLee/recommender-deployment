"""gunicorn server configuration."""
import os

threads = 20
workers = 1
timeout = 0
host = "0.0.0.0"
bind = f":{os.environ.get('PORT', '10000')}"
worker_class = "uvicorn.workers.UvicornWorker"
