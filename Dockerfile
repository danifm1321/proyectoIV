FROM python:3.8-slim-buster

LABEL manteiner="danifm1321"

RUN groupadd -r testuser && useradd -m -r -g testuser testuser
USER testuser

WORKDIR /app/test

COPY pyproject.toml poetry.lock tasks.py /app/

ENV PATH=$PATH:/home/testuser/.local/bin
RUN pip3 install poetry; poetry config virtualenvs.create false; poetry install

ENTRYPOINT ["invoke", "test"]
