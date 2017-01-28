.PHONY: build run stop clean

FLAGS=#--debug

build:
	ansible-container $(FLAGS) build

run:
	ansible-container run

stop:
	ansible-container stop

# Delete images
clean:
	docker ps -a | awk 'NR!=1 { print $1 }' | xargs docker rm
	docker images | awk 'NR>1' | awk '/ch13.*/ {print $1":"$2}' | xargs docker rmi
