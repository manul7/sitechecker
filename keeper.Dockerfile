FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY siteprobe /app
ENV MTYPE availability
CMD python /app/keeper.py $MTYPE
