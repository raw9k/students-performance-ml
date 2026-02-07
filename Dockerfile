FROM python:3.11-slim

WORKDIR /app
COPY . /app

# If you don't need OS packages, you can remove apt entirely.
# If you do need OS packages, install them here (example keeps it minimal).
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]

