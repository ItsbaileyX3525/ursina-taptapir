from ursina import *
import socketio

taptapPos = []

sio = socketio.Client()

sio.connect('http://localhost:6787')


def sendUrsinaPos(pos):
    sio.emit('updateUrsinaPosition', list(pos))

@sio.on("TaptapPos")
def recieveTaptapPos(pos):
    global taptapPos
    taptapPos = pos


app=Ursina(borderless=False)

mainPlayer = Entity(model="circle", color=color.red,scale=.1,parent=camera.ui)

otherPlayer = Entity(model="circle", color=color.blue,scale=.1,parent=camera.ui,y=-.1)

def update():
    global taptapPos
    if held_keys['w']:
        mainPlayer.y+=.005
    if held_keys['a']:
        mainPlayer.x-=.005
    if held_keys['s']:
        mainPlayer.y-=.005
    if held_keys['d']:
        mainPlayer.x+=.005
    
    sendUrsinaPos(mainPlayer.position)

    otherPlayer.position = taptapPos


app.run()


