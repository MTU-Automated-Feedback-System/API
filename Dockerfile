FROM python:3.10
WORKDIR /opt/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD ["python3.10", "app.py"]
