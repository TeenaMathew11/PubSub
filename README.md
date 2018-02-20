# PubSub
Basic publish-subscribe API

I have written a basic publish-subscribe API using Python. I have implemented all the functionalities that has to provided, assuming that there is only one Publisher and Subcriber. For keeping the logic simple I have not used any external databases to store the topics; so they are stored in the application itself and accessible only when the application is running. Currently I have not implemented any logic for the subcriber to automatically receive a note to the topics subcribed, when a new note is posted for a subscribed topic. Only when the subscriber explicity requests for topic it is send.

I used Postman for testing the implementation and I hope it will be clear from the video.

I used Python to write this because I feel it is easy to implement the logic in this language. The code is extremely readable at the same time we can implement a relatively complex logic in fewer lines of code. Its library provides us with a large number of tools which makes the tasks easier. It is very easy to interface with internet and it supports HTTP.

I used the Flask framework because it gives good access to ports in our own system or on internet. It can format HTML, JSON etc. So in this case since the application implements only a basic publish-subscribe API and with Flask we do not require many additional tools and it supports the HTTP methods. 
