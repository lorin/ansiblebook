.PHONY: build start run stop clean

# Generate self-signed certs for localhost
ssl: certs/nginx.crt certs/nginx.key

certs/nginx.crt certs/nginx.key:
	openssl req -new -x509 -nodes -out certs/nginx.crt -keyout certs/nginx.key -subj '/CN=localhost' -days 3650
