from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
socketio = SocketIO(app, cors_allowed_origins="*", max_http_buffer_size=16 * 1024 * 1024)


@app.route('/')
def index():
    return render_template('index.html')

@socketio.on("updateUrsinaPosition")
def sendUrsinaPosToTaptap(pos):
    socketio.emit("UrsinaPos",pos)
    print("Ursina pos: ",pos)

@socketio.on("updateTaptapPosition")
def sendTaptapPosToUrsina(pos):
    socketio.emit("TaptapPos", pos)


if __name__ == '__main__':
    socketio.run(app,host="0.0.0.0",port=6787, debug=True)
