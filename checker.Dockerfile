FROM python:3.10-slim
WORKDIR /app
COPY siteprobe.project/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY siteprobe.project/siteprobe /app
CMD python /app/probe.py
