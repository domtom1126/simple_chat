from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/', methods=['GET', 'POST'])
def sessions():
    return render_template('session.html')

def message_receivied(methods=['GET', 'POST']):
    print('message received')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET','POST']):
    print('event received' + str(json))
    socketio.emit('my response', json, callback=message_receivied, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)

