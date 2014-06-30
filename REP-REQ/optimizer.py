import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
addr = "tcp://localhost:5555"

print "Connecting to simulation: " + addr
socket.connect(addr)

params = b"Q = 5"
print "Sending params: " + params
socket.send(params)

print("Waiting on recv")
message = socket.recv()
print("Received loss [ %s ]" %  message)

