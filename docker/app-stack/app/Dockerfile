FROM python:3.12-alpine

WORKDIR /app

# optional, aber sauber: unprivilegierter user
RUN adduser -D -h /app appuser
USER appuser

COPY app.py /app/app.py

EXPOSE 8000

CMD ["python", "/app/app.py"]
