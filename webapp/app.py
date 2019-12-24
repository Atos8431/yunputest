import os

from flask import Flask
import time
import socket


app = Flask(__name__)


@app.route('/')
def hello():
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    return "Time: %s Host: %s IP: %s" % (time.asctime(time.localtime(time.time())), host, ip)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
