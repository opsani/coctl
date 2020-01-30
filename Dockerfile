FROM python:alpine
LABEL maintainer="robert@kumul.us"
LABEL description="A wrapper around coctl to simplify installation"

ENV CO_TOKEN='' CO_DOMAIN='' CO_APP=''

WORKDIR /work
COPY . .
RUN pip install -U pip
RUN pip install .
ENTRYPOINT ["coctl"]
CMD ["--help"] 
