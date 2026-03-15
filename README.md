# HTTP vs HTTPS

HTTP (HyperText Transfer Protocol) is used to transfer data between a client and a server.  
It does not encrypt the data, which means that attackers can see the information.

HTTPS (HyperText Transfer Protocol Secure) is the secure version of HTTP.  
It uses SSL/TLS encryption to protect the data transmitted between the client and the server.

HTTPS is commonly used for secure websites such as banking, login pages, and email services.

---

# HTTP Request Structure

An HTTP request contains:

- Request Line
- Headers
- Body (optional)

Example:

GET /index.html HTTP/1.1  
Host: example.com  

---

# HTTP Response Structure

An HTTP response contains:

- Status Line
- Headers
- Body

Example:

HTTP/1.1 200 OK  
Content-Type: text/html  

---

# Common HTTP Methods

GET – Retrieve data from the server  
POST – Send new data to the server  
PUT – Update existing data  
DELETE – Remove data from the server  

---

# Common HTTP Status Codes

200 OK – The request was successful  
301 Moved Permanently – Resource moved to a new URL  
400 Bad Request – The request is invalid  
404 Not Found – The requested resource was not found  
500 Internal Server Error – Server encountered an error
