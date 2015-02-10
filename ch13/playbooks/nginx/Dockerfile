FROM debian:wheezy
# From
# https://github.com/nginxinc/docker-nginx/blob/57da11369acbec3256b0c2704a50282eeabb684f/Dockerfile

# We repeat rather than do it from this one because of
# https://github.com/docker/docker-py/issues/447


RUN apt-key adv --keyserver pgp.mit.edu --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62
RUN echo "deb http://nginx.org/packages/mainline/debian/ wheezy nginx" >> /etc/apt/sources.list

ENV NGINX_VERSION 1.7.9-1~wheezy

RUN apt-get update && apt-get install -y nginx=${NGINX_VERSION} && rm -rf /var/lib/apt/lists/*

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

# See Docker bug referenced at the top
# VOLUME ["/var/cache/nginx"]

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]

RUN rm /etc/nginx/conf.d/default.conf \
       /etc/nginx/conf.d/example_ssl.conf
COPY nginx.conf /etc/nginx/conf.d/mezzanine.conf
