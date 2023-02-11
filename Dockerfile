FROM python:3.10-alpine
WORKDIR /opt/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080CMD
CMD["cd","src","&&","gunicorn", "wsgi:app", "-w $(( 2 * `nproc` + 1 ))", "-b 0.0.0.0:8080"]
