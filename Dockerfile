FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir cherrypy requests
EXPOSE 8080
CMD ["python", "__main__.py"]
