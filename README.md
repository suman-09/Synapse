# **API**
 API is acronym  for Application Programming Interface, which is a software intermediary that allows two applications to talk to each other.

 In this project we are making an application using python that will help in fetching and testing APIs using various libraries of python.
***
 **Approach for building an API Tester**

 This project will enable us to perform the following functions on API:
1. GET
1. POST
1. AUTH
1. PUT
### **GET:**
 A GET request, in simple terms, is a way for you to grab data from a data source with the help of the internet.

### **POST:**

 POST is used to send data to a server to create/update a resource.

### **PUT:**

 PUT is used to send data to a server to create/update a resource.


 The difference between POST and PUT is that PUT requests are idempotent. That is, calling the same PUT request multiple times will always produce the same result. In contrast, calling a POST request repeatedly have side effects of creating the same resource multiple times.
***
## In this project we are using mainly the following python libraries:-
 1. REQUESTS
 1. TKINTER

 ## **REQUESTS**
 ***

One of the main working of this application is to bring data or information from any API and display it to the user. The task of sending HTTP requests using Python is performed using the “Requests” Module. 

 The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).

 The first step in using this module is to import it in the python file.

 ### Run the following command to import this library:
```
pip install requests
```
<!-- ### Throughout this project we will be using various functions of **REQUESTS** library for fetching and sending data to server.  -->

 Once our HTTP requests are working properly and we are able to fetch data from the API, we need a proper interface to send and receive a request. And for this purpose, we have the Tkinter library in python.
## **TKINTER**
***

 Tkinter is a python library including multiple modules which is used for making GUI for any python application.
