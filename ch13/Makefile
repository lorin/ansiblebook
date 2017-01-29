.PHONY: build start run stop clean

FLAGS=#--debug

build:
	ansible-container $(FLAGS) build

run:
	ansible-container run

start: run

stop:
	ansible-container stop

# Delete images
clean:
	docker ps -a | awk 'NR!=1 { print $1 }' | xargs docker rm
	docker images | awk 'NR>1 && /ch13.*/ {print $1":"$2}' | xargs docker rmi

# Generate self-signed certs for localhost
ssl: certs/nginx.crt certs/nginx.key

certs/nginx.crt certs/nginx.key:
	openssl req -new -x509 -nodes -out certs/nginx.crt -keyout certs/nginx.key -subj '/CN=localhost' -days 3650
