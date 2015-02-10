.PHONY: image run bash

IMAGE=lorin/nginx-mezzanine

image:
	docker build -t $(IMAGE) .

bash:
	docker run -ti $(IMAGE) /bin/bash

