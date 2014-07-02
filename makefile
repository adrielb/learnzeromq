all: push-pull

push-pull:
	python PUSH-PULL/simulation.py &
	python PUSH-PULL/simulation.py &
	python PUSH-PULL/optimizer.py

rep-req:
	python REP-REQ/simulation.py &
	python REP-REQ/optimizer.py &

clone-examples:
	git clone --depth=1 git://github.com/imatix/zguide.git
