FROM python:3.6.5-slim

LABEL Author="Daniel Porfiiro 'me@danielporfirio.com'"

ENV ENVIRONMENT 'development'

WORKDIR /{{cookiecutter.package_name}}

COPY . .

RUN pip3 install --upgrade pip \
    && pip3 install -r requirements/docker.txt

EXPOSE 8000

ENTRYPOINT ["/usr/local/bin/gunicorn", "-b", ":8000", "app:create_app()"]