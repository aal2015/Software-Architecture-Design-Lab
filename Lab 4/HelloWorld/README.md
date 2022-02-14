<h1> Build container image </h1>
docker build --tag hello-world-django .

<h1> Run container </h1>
docker run -d -p 8000:8000  hello-world-django
