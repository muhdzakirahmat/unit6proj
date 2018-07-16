FROM python:2.7-alpine
RUN apk update && \
    apk add python python-dev libffi-dev gcc make musl-dev py-pip mysql-client

RUN mkdir -p /opt/Unit6
COPY . /opt/Unit6
WORKDIR /opt/Unit6
VOLUME ["/opt/Unit6"]

RUN pip install -r requirements.txt
RUN for d in Unit6/plugins/*; do \
      if [ -f "$d/requirements.txt" ]; then \
        pip install -r $d/requirements.txt; \
      fi; \
    done;

RUN chmod +x /opt/Unit6/docker-entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/opt/Unit6/docker-entrypoint.sh"]
