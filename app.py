from flask import Flask, render_template, request
import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    server = request.host_url
    ip = request.remote_addr
    agent = request.headers.get('User-Agent')
    return render_template('index.html', server=server, ip=ip, agent=agent)
    

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)