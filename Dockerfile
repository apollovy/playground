FROM python:3.5

MAINTAINER apollovy@gmail.com

# Content-independent
RUN pip install --upgrade pip

# Content-dependent
COPY ./requirements /tmp/requirements
RUN pip install -r /tmp/requirements/pip/default.txt
RUN mkdir -p /app/fmc
COPY ./fmc /app/fmc

ENTRYPOINT
ENV PYTHONPATH=/app
CMD python /app/fmc/main.py
