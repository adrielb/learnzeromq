* zmq strings are length-specified and are sent on the wire w/o a trailing null
* zhelpers.h - C string helper functions
* each send() expects a recv()
* recv() are blocking
* sends() are appended to queue
* reactor (zloop) vs polling
* pub - sends are all of many
  * pub-sub profoundly aimed at scalability
  * recipients dont talk back to senders
  * gain scalability, lose coordination btw sender and receiver
* Push/dealer - rotate msgs to one of many
* Push sockets distributes msgs evenly
  * slow joiner - worker that connects first gets all the msgs
  * BUG: unsent msgs get thrown away if socket closes unexpectedly (LINGER)
