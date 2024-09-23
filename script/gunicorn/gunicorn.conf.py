import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
bind = '0.0.0.0:8000'
worker_class = "gthread"
threads = 4
timeout = 60