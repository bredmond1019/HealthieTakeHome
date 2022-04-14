# HealthieTakeHome


Hey Healthie Team!

I really enjoyed this take home. It was the right amount of challenging where I had to think but still had a lot of fun.

The short answer questions are answered at the bottom.

I chose to do my solutions for the coding challenges in _Python_. Each of the challenges are in their own subdirectory.

### Prime Number Finder

This one should be pretty self explanatory -- you just need to run the _prime_number_finder.py_ file and it will display the last prime in the terminal. I noticed when soliving it that I got a different answer each time, but generally they were in the same ballpark, somewhere around: _39615311_.


### Class Design Problem

The main file that you will need to run is the _animals_eating.py_ file. In this file, I instantiate all of the classes and then show each of the animals eating each of the food items. You can feed the animals either an instance of the class, or the actual class itself, and it will provide the same outcome. As the file is now, the animals are eating instances of the Food class. Feel free to uncomment the section at the bottom to see them eating the actual class as a whole.

I provided each food class a class attribute called name, as well as an instance attribute called name in case you wanted name the particular item of food (pizza, puppy chow, etc). Also, you can name the animals if you'd like.



### Model Design Problem

This challenge was really fun. I had to think a bit at first on how to create the models, but then it clicked and made sense. I created a backend API using Flask and GraphQL. I utilized flask's application factory format to allow dynamic configurations for development, testing, and production. Everything is basically done using GraphQL, but I did include a REST API blueprint to easily add enpoints if needed.

I also created _unittest_ s for the queries you asked for. In the _ModelDesignProblem_ directory, there will be a subdirectory called _tests_. In this file you can see how I formated the queries you asked for as well as the output you should see. Instructions on how to run the tests are below in the SETTING UP FLASK section

When I created my own Postgres Database and added the data that way, I was able to get the journal entries to be ordered in decreasing dates, so the newest entries were first. However, in the SQLite database, each time I made a query it restamped the time for the journal entry and they all had the exact same time. Feel free to create a normal postgres database to check it out instead of using the in-memory sequal lite that I provided. Also, I had some trouble testing the dates using the SQLite database, I believe it has something to do with the datetime format being miliseconds off, but I didn't want to spent too much time on that.

Let me know if you have any questions. I left instructions for how to set up the environment below.

Looking forward to our review!


#### Setting Up the Flask Environment

I code on a linux machine, so all of the commands are for a linux operating system. They should be similar for a Mac.

Also, in the requirements.txt file, I commented out line 29 -- psycopg. If you are using a _Mac_ , leave it commented out and it should run fine. If you are using Linux, you will probably have to uncomment out line 29. I tested it on both and that is what I had to do. 

1. Go into the __ModelDesignProblem__ directory
2. Make sure you have python>=3.6 installed. I was using 3.8 at the time.
3. You'll want to set up a `venv` --> `python3 -m venv healthieVenv`
4. Once the environment is created, activate the environment --> `source healthieVenv/bin/activate`
5. Install the packages required -->  `pip install -r requirements.txt`
6. In the command line on your terminal you'll want to enter the following:
   - `export FLASK_APP=app.py`
   - `export FLASK_DEBUG=1`
   - `flask test` _This will run the tests_
   - `flask run` _You can run this after the tests if you want to activate the flask server_
   - You can head to `http://localhost:5000/` and you should see some JSON with all of the users, providers, their journal entires, and the plan with that specific provider. This was the only REST API endpoint I made. The rest is GraphQL.
   - If you go to `http://localhost:5000/graphql` you will see the GraphiQL window to make some _queries_ and _mutations_
   - You should be able to use this window to play around and make all of the queries you asked for.





### SHORT ANSWER

1) **What is HTML?**
- Hyper Text Markup Language
- It is similar to XML for android, etc
- Used to organize the layout of the view on the client side (browser) using tags
- Div, img, p, ul, ol, etc.


2) **What is CSS?**
- Cascading Style Sheets
- Used to style the HTML elements  (colors, borders, backgrounds, size, etc)
- Flexbox & Grid are commonly used for better layout organization
- The further down the style sheet you go, these items have precedence.
- Can use media queries to format view with different screen sizes


3) **What is the DOM?**
- Document Object Model
- Allows languages like Javascript to interact and manipulate the page and DOM
- React uses a virtual DOM to increase performance over the regular DOM that the browser manipulates


4) **What is memory?**
- Also known as RAM
- A bunch of addresses, each with 8 bits (1 byte)
- The processor makes calls to the addresses in memory when it needs information
- The processor caches that call, as well as other addresses nearby. This is why an array will typically have faster call time than say a linked list where all the addresses may be randomly spread throughout


5) **What is TCP/IP?**
- Transmission Control Protocol / Internet Protocol
- Set of rules on how computers can talk to each other
- Each computer has a unique IP address
- Opens a connection between two IP addresses, much like a phone line, to send packets of data between two IP addresses.


6) **In a programming language, what is a class?**
- A class is an object that provides a structure and allows a program to keep some sort of state. Allowing real world concepts to be written in code that is closely related to how we think of objects.
- Classes have attributes and methods
- We can create object Instances of each class that will be unique to other instances, but may share class attributes and methods.
- Classes can be abstracted and built as a blueprint that other classes can inherit from. Or we can encapsulate our classes to hide away some of the logic and use some sort of factory to implement the class.


7) **In a database, what is a foreign key?**
- A foreign key is number that associates a model of one table to a model of another table
- If I have two models, say User and Role.  Each user will have a specific role (admin, moderator, user, etc). So in the user model, we will have a foreign key associated with the Role model to establish the relationship
- Refers to the primary key of the other table


8) **What is Model View Controller?**
- A way to design an application
- The model is the real world object that we are dealing with, the data.
- The view is what the user sees and interacts with on the client side
- The controller is the logic that manipulates the data and decides what to do with the data. It’s the intermediary between the model and the view.

