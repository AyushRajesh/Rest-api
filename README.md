# REST-API
Rest_API to Insert and Retrieve some data from a database table.

## What is a Rest API?

- A RESTful API uses HTTP  requests to GET, PUT, POST, DELETE data the following the REST standards.
- This allows two pieces of software to communicate with each other.

## REST API example application

1. This is a bare_bones example of a books application providing a REST API to a database.
2. The entire application is contained within the **school.py** file.
3. **book.sql** is the database stored for the entire Application.
4. We have used the **MYSQL DATABASE**.
5. We have used **Postman** which is a scalable API testing tool to test API.

### Paths
 A good RESTful design has a pattern for the URL, such that:
- GET:/books- Returns an arrary of "book" record.
- GET:/books/id- Gets a specific "book" record.
- PUT:/books/id- Updates a specific "book" record.
- POST:/books/- Creates a new "book" record.
- DELETE:/book/id-Deletes a "book" record.

### Response Codes
The more detail the better here, but if I at least hear:
- **200**- Success.
- **201**- Created.
- **300**- Proxies handle it.
- **400**- Error.
- **401**- Not Authorized.
- **404**- Not found.
- **500**- Internal Server Error.
- and more on [https://www.restapitutorial.com/httpstatuscodes.html]()

# About Project

I have created a REST API which get, update, delete, create  book records in the book database. We use request methods such as GET, POST, PUT, DELETE to perform operations on the book records stored in the database by HTTP Response. I have made this entire project in Python using Flask and MYSQL Database.

## Run install

To run the API, we need to install some module
- First of all, Create a folder then open the folder and write the following command in command prompt to create virtual environment.
 ```PYTHON
 python -m venv venv
 ```
 - Now, open the script folder in venv folder then copy paste the activate file in command prompt and press enter.
 - Now it's time to download the modules which we are going to use in program code. 
 - To install **Flask** open the command prompt and write the command:-
  ```PYTHON
 pip install flask
 ```
 - Here we have used the **MYSQL** database in python. So, to install **Pymysql** open the command prompt and write the command:-
  ```PYTHON
 pip install Pymysql
 ```
 ## RUN school
 
  ```PYTHON
 python school.py
 ```
After running the program we get
``` PYTHON
* Serving Flask app 'school' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 107-463-888
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Just copy the http://127.0.0.1:5000/ and run it in the browser or in the postman app to test the different methods.

# Get list of Books

## Request
```PYTHON
GET/books/
```

```PYTHON
http://127.0.0.1:5000/books
```
## Response

```PYTHON
127.0.0.1 - - [19/Jun/2021 14:44:22] "GET /books HTTP/1.1" 200 -
```
```PYTHON
[
  {
    "author": "\tVita Sackville-West", 
    "id": 1, 
    "language": "English", 
    "title": "All Passion Spent"
  }, 
  {
    "author": "Madeleine L Engle", 
    "id": 2, 
    "language": "English", 
    "title": "An Acceptable Time"
  }, 
  {
    "author": "Robert Penn Warren", 
    "id": 3, 
    "language": "English", 
    "title": "All the Kings Men"
  }
  ]
```

# Create a new book

## Request
```PYTHON
POST/books/
```

```PYTHON
http://127.0.0.1:5000/books
```
## Response

```PYTHON
127.0.0.1 - - [19/Jun/2021 14:50:26] "POST /books HTTP/1.1" 200 -
```
```PYTHON
Book details created successfully
```

# Get a specific book

## Request
```PYTHON
GET/book/id
```

```PYTHON
http://127.0.0.1:5000/book/id
```
## Response

```PYTHON
127.0.0.1 - - [19/Jun/2021 14:50:26] "GET/book/2 HTTP/1.1" 200 -
```
```PYTHON
{
  "author": "Madeleine L Engle", 
  "id": 2, 
  "language": "English", 
  "title": "An Acceptable Time"
}
```

# Get a non-existent book

## Request
```PYTHON
GET/book/id
```

```PYTHON
http://127.0.0.1:5000/book/id
```
## Response

```PYTHON
127.0.0.1 - - [19/Jun/2021 14:54:46] "GET /book/14 HTTP/1.1" 404 -
```
```PYTHON
No Book record for this id.
```

# Change a Book's state

## Request
```PYTHON
PUT/book/id
```

```PYTHON
http://127.0.0.1:5000/book/id
```
## Response

```PYTHON
127.0.0.1 - - [19/Jun/2021 14:54:47] "PUT /book/14 HTTP/1.1" 200 -
```
```PYTHON
Book with id 14 has been updated successfully
```

# Delete a book

## Request
```PYTHON
DELETE/book/id
```

```PYTHON
http://127.0.0.1:5000/book/id
```
## Response

```PYTHON
127.0.0.1 - - [19/Jun/2021 14:54:47] "DELETE /book/14 HTTP/1.1" 200 -
```
```PYTHON
The book with id: 14 has been deleted.
```

# Try to delete same book again

## Request
```PYTHON
DELETE/book/id
```

```PYTHON
http://127.0.0.1:5000/book/id
```
## Response

```PYTHON
127.0.0.1 - - [19/Jun/2021 14:54:49] "DELETE /book/14 HTTP/1.1" 404 -
```
