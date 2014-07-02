import zmq

context = zmq.Context()

pull_addr = "tcp://127.0.0.1:5557"
print "Simulation connecting to " + pull_addr
pull_socket = context.socket(zmq.PULL)
pull_socket.connect(pull_addr)

push_addr =  "tcp://127.0.0.1:5558"
print "Simulation connecting to " + push_addr
push_socket = context.socket(zmq.PUSH)
push_socket.connect(push_addr)

results = {}
while True:
    params = pull_socket.recv_json()
    print "Recieved params: " + str(params)

    results['L'] = params['a'] * params['a']

    push_socket.send_json( results )