# HealthieTakeHome

### SHORT ANSWER

1) What is HTML?
- Hyper Text Markup Language
- It is similar to XML for android, etc
- Used to organize the layout of the view on the client side (browser) using tags
- Div, img, p, ul, ol, etc.


2) What is CSS?
- Cascading Style Sheets
- Used to style the HTML elements  (colors, borders, backgrounds, size, etc)
- Flexbox & Grid are commonly used for better layout organization
- The further down the style sheet you go, these items have precedence. 
- Can use media queries to format view with different screen sizes


3) What is the DOM?
- Document Object Model
- Allows languages like Javascript to interact and manipulate the page and DOM
- React uses a virtual DOM to increase performance over the regular DOM that the browser manipulates


4) What is memory?
- Also known as RAM
- A bunch of addresses, each with 8 bits (1 byte)
- The processor makes calls to the addresses in memory when it needs information
- The processor caches that call, as well as other addresses nearby. This is why an array will typically have faster call time than say a linked list where all the addresses may be randomly spread throughout


5) What is TCP/IP?
- Transmission Control Protocol / Internet Protocol 
- Set of rules on how computers can talk to each other
- Each computer has a unique IP address
- Opens a connection between two IP addresses, much like a phone line, to send packets of data between two IP addresses. 


6) In a programming language, what is a class?
- A class is an object that provides a structure and allows a program to keep some sort of state. Allowing real world concepts to be written in code that is closely related to how we think of objects. 
- Classes have attributes and methods
- We can create object Instances of each class that will be unique to other instances, but may share class attributes and methods.
- Classes can be abstracted and built as a blueprint that other classes can inherit from. Or we can encapsulate our classes to hide away some of the logic and use some sort of factory to implement the class. 


7) In a database, what is a foreign key?
- A foreign key is number that associates a model of one table to a model of another table
- If I have two models, say User and Role.  Each user will have a specific role (admin, moderator, user, etc). So in the user model, we will have a foreign key associated with the Role model to establish the relationship
- Refers to the primary key of the other table


8) What is Model View Controller?
- A way to design an application
- The model is the real world object that we are dealing with, the data. 
- The view is what the user sees and interacts with on the client side
- The controller is the logic that manipulates the data and decides what to do with the data. It’s the intermediary between the model and the view. 
