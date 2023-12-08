.PHONY: run-servers run-lb

run-lb:
	./main --backends=http://localhost:3031,http://localhost:3032,http://localhost:3033

run-server1:
	python server1.py

run-server2:
	python server2.py

run-server3:
	python server3.py
