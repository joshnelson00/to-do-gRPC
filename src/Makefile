.PHONY: proto clean

proto:
	python -m grpc_tools.protoc \
		-I./proto \
		--python_out=./pb \
		--grpc_python_out=./pb \
		proto/*.proto

clean:
	rm -rf pb/*.py
	rm -rf pb/__pycache__

install:
	pip install grpcio grpcio-tools protobuf

all: clean proto