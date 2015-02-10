.PHONY: image bash

IMAGE=lorin/certs

image:
	docker build -t $(IMAGE) .

bash:
	docker run -ti $(IMAGE) /bin/bash

