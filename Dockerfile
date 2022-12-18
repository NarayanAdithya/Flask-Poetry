FROM python:3.9.15-alpine3.16
WORKDIR /flaskapp
COPY pyproject.toml pyproject.toml
COPY runner.py runner.py
ADD app /flaskapp/app
COPY poetry.lock poetry.lock
COPY README.md README.md
RUN pip install poetry
RUN poetry config virtualenvs.in-project true
RUN poetry install --without dev
EXPOSE 5000
CMD [".venv/bin/python3","-m","gunicorn","--bind","0.0.0.0:5000","runner:app"]
