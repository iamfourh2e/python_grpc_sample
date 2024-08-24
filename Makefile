.PHONY: clean
clean:
	@echo "Cleaning up..."
	@rm -rf pb/*

.PHONY: proto
proto: clean
	@echo "Generating protobuf files..."
	@python -m grpc_tools.protoc -I=./proto --python_out=./pb --pyi_out=./pb --grpc_python_out=./pb ./proto/*.proto
