# python-flask-api
Sample of simple APIs using flask

### Installing dependencies
To install, just type:

    pip3 install -r requirements.txt

### Run
Start the rest server typing:
    python3 src/api.py

It will serve at localhost:8080

### Testing
You can test it using Postman or insomnia, or also just using curl

GET v1/hello
```
    curl http://localhost:8080/v1/hello
```

POST v1/echo
```
    curl -X POST -H "Content-Type: application/json" --data "{\"test\": \"sample message\"}" http://localhost:8080/v1/echo
```