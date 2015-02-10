.PHONY: image bash

IMAGE=lorin/memcached

image:
	docker build -t $(IMAGE) .

bash:
	docker run -ti $(IMAGE) /bin/bash

