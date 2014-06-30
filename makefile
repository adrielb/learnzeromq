all: rep-req

rep-req:
	python REP-REQ/simulation.py &
	python REP-REQ/optimizer.py &

clone-examples:
	git clone --depth=1 git://github.com/imatix/zguide.git
