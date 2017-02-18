.PHONY: start publish build local facts deploy

deploy:
	ansible-playbook deploy.yml -l ghost --start-at-task 'create network'

facts:
	ansible-playbook image-facts.yml

start: local

stop:
	docker-compose kill
	docker-compose rm --forc

local:
	ansible-playbook local.yml

publish: build
	ansible-playbook publish.yml

build:
	ansible-playbook build.yml

clean:
	ansible-playbook clean.yml

# Generate self-signed certs for localhost
ssl: certs/nginx.crt certs/nginx.key

certs/nginx.crt certs/nginx.key:
	openssl req -new -x509 -nodes -out certs/nginx.crt -keyout certs/nginx.key -subj '/CN=localhost' -days 3650
