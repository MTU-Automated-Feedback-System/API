FROM python:3.10-alpine
WORKDIR /opt/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["python3.10", "app.py"]
