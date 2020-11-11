FROM python:3.7-slim-stretch

COPY Pipfile Pipfile.lock /tmp/pipenv/

COPY ./ /flask

WORKDIR /flask

RUN apt update && \
	apt install -y gcc libmariadbclient-dev && \
	pip install pipenv && \
	pipenv install

ENTRYPOINT ["bash"]