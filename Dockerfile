FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir .

ENTRYPOINT ["termatplotlib"]
CMD ["--help"]
