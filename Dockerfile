FROM python:alpine
LABEL maintainer="robert@opsani.com"
LABEL description="A simple Docker python wrapper around coctl to simplify installation"
LABEL version="0.2.0"

ENV CO_TOKEN='' CO_ACCOUNT='' CO_APP=''

WORKDIR /work
COPY . .
RUN pip install -U pip .
ENTRYPOINT ["coctl"]
CMD ["--help"] 
