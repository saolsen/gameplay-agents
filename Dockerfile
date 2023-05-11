FROM python:3.11-slim-bullseye as prod
COPY . .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir 'fastapi[all]'
CMD ["uvicorn", "gameplay_agent:build_app", "--factory", "--proxy-headers", "--forwarded-allow-ips", "*", "--host", "0.0.0.0", "--port", "8000"]
