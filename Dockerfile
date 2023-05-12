FROM python:3.12.0a7-alpine3.18
WORKDIR /app
COPY *.py /app/
COPY *.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt
CMD ["python", "/app/e2e.py"]
