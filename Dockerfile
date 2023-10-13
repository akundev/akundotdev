FROM python:3.12-slim

LABEL org.opencontainers.image.source=https://github.com/akundev/akundotdev

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY Pipfile Pipfile.lock ./
RUN \
    pip install pipenv gunicorn  && \
    pipenv install --deploy --ignore-pipfile --system

COPY apps settings static templates manage.py ./

ENTRYPOINT ["gunicorn"]
CMD ["--bind", "0.0.0.0:8000", "settings.wsgi:application", "-w", "4", "--threads", "10" ]
