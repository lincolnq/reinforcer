from flask import Flask
app = Flask(__name__)

import fabfile

@app.route("/reward")
def reward():
    from fabric.api import env
    env.host_string = 'rpi'
    reload(fabfile)
    fabfile.step()

    return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=48001)
