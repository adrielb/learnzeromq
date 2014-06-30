import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
addr = "tcp://*:5555"

print "Binding to " + addr
socket.bind(addr)

for i in range(1):
    #  Block for next params from client
    message = socket.recv()
    print("Received params: %s" % message)

    #  Do some 'work'
    time.sleep(1)

    loss = b"L = 41"
    print "Sending loss: " + loss
    socket.send(loss)
