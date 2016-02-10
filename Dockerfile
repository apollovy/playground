FROM python:3.5

MAINTAINER apollovy@gmail.com

# Content-independent
RUN pip install --upgrade pip

# Content-dependent
COPY ./requirements /tmp/requirements
RUN pip install -r /tmp/requirements/pip/default.txt
COPY ./app /app

ENTRYPOINT
CMD python /app/main.py
