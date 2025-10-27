FROM python:3.13-alpine AS builder

WORKDIR /app

RUN pip install --no-cache-dir pipenv==2024.4.0 daphne==4.1.2 

COPY Pipfile Pipfile.lock ./
RUN PIPENV_VENV_IN_PROJECT=1 \
    pipenv install --deploy --ignore-pipfile --system

COPY . .
RUN python ./manage.py collectstatic --noinput

FROM python:3.13-alpine
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=0 


LABEL org.opencontainers.image.source=https://github.com/akundev/akundotdev

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin/daphne /usr/local/bin/daphne
COPY --from=builder /app/staticfiles ./staticfiles
COPY --from=builder /app/apps ./apps
COPY --from=builder /app/settings ./settings
COPY --from=builder /app/templates ./templates
COPY --from=builder /app/manage.py ./

RUN addgroup -S appgroup && \
    adduser -S appuser -G appgroup && \
    chown -R appuser:appgroup /app

USER appuser

ENTRYPOINT [ "daphne" ]
CMD [ "settings.asgi:application", "-b", "0.0.0.0", "-p", "8000" ]