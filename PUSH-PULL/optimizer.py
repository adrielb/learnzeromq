import zmq
import time

context = zmq.Context() 

push_addr = "tcp://127.0.0.1:5557"
print "Optimizer binding to " + push_addr
push_socket = context.socket(zmq.PUSH)
push_socket.bind(push_addr)


pull_addr = "tcp://127.0.0.1:5558"
print "Optimizer binding to " + pull_addr
pull_socket = context.socket(zmq.PULL)
pull_socket.bind(pull_addr)

# wait for simulation processes to spin up 
time.sleep(1)

# send params to simulators
for i in range(4):
    params =  { 'a' : i } 
    print "Sending: " + str(params)
    push_socket.send_json(params)

for i in range(4):
    result = pull_socket.recv_json()
    print "Recieved result: " + str(result)

time.sleep(1)

