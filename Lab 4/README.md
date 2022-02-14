<!-- Build container image-->
docker build --tag hello-world-django .

<!-- Run container -->
docker run -d -p 8000:8000  hello-world-django
