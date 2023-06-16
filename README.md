<h1 style="text-align: center;">APIs</h1>

## API Basics
APIs (Application Programming Interfaces) are sets of rules and protocols that allow different software applications to communicate with each other. They define the methods and data formats that should be used for requesting and exchanging information between applications.

### How are they used and why are they so popular?
APIs are used to enable the integration of different systems and services. They provide a standardized way for applications to interact and exchange data, regardless of the technologies used or the platforms they are built upon. APIs have gained popularity because they simplify software development, promote reusability, and allow organizations to expose their services to external developers or partners in a controlled manner.

### Data Transfer Process in API Communication
![](https://s33046.pcdn.co/wp-content/uploads/2021/03/representational-state-transfer-diagram_gray-e1615546557211.png)

## REST API

### What is a REST API?
REST (Representational State Transfer) API is an architectural style for designing networked applications. It is based on a set of principles that emphasize scalability, statelessness, and uniformity in resource representation and manipulation.

### What makes an API RESTful?
To be considered RESTful, an API should adhere to several principles, including:

1. Client-Server Architecture: The client and server are separate entities that communicate over a network.
2. Stateless Interaction: Each request from a client to a server contains all the necessary information for the server to understand and process the request. The server does not retain any information about the client's previous requests.
3. Uniform Interface: The API should have a consistent and standardized interface, typically using HTTP methods (verbs) and resource-based URLs.
4. Cacheability: Responses from the server can be cached by the client to improve performance.
5. Layered System: The API can be composed of multiple layers, with each layer providing a specific set of functionality.

## HTTP

### What is HTTP?
HTTP (Hypertext Transfer Protocol) is a protocol that defines how clients and servers communicate over the web. It is the foundation of data communication on the World Wide Web.

### What does HTTP stand for and what is it used for?
HTTP stands for Hypertext Transfer Protocol. It is used for the transmission of various types of data, such as HTML pages, images, videos, and other resources, between web browsers (clients) and web servers.

### What is HTTPS?
HTTPS (HTTP Secure) is the secure version of HTTP. It adds encryption and authentication mechanisms to the communication protocol, providing a secure and encrypted connection between clients and servers.

### HTTP Request Structure

An HTTP request consists of:
- **Method/Verb**: Specifies the type of action to be performed on the resource (e.g., GET, POST, PUT, PATCH, DELETE).
- **URL/URI**: Identifies the resource to be acted upon.
- **Headers**: Additional metadata or instructions for the server.
- **Body**: Optional data sent along with the request, typically used for POST or PUT requests.

### HTTP Response Structure

An HTTP response consists of:
- **Status Code**: Indicates the outcome of the request (e.g., 200 OK, 404 Not Found, 500 Internal Server Error).
- **Headers**: Additional metadata or instructions from the server.
- **Body**: Contains the requested resource or any error messages.

### HTTP Verbs
The 5 commonly used HTTP verbs and their purposes are:

1. **GET**: Retrieves a representation of the specified resource.
2. **POST**: Submits data to be processed to the specified resource.
3. **PUT**: Updates the specified resource with the provided data.
4. **PATCH**: Partially
