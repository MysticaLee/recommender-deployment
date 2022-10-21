"""gunicorn server configuration."""
import os

threads = 2
workers = 2
timeout = 0
host = "0.0.0.0"
bind = f":{os.environ.get('PORT', '3000')}"
worker_class = "uvicorn.workers.UvicornWorker"
