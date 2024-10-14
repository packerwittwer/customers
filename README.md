## Overview

**Customer Database**:

**A cloud database to hold the relevant info for customers of my side hustle. For your info, I make chainmail/scalemail bags for people to hold their DnD dice in (or coins or whatever else).**:

**Create one place to keep all the info on orders.**:

## Instructions for Build and Use

Steps to build and/or run the software:

1. Import libraries
2. Connect to database
3. Create main function
4. Create other functions (for each option)
5. Create a dictionary to hold the functions in step 4
6. Test piece by piece, one function at a time

Instructions for using the software:

1. Choose an option/response (usually a number to declare your choice)
2. Fill out any required fields
3. Press enter to submit your choice/response
4. Repeat as desired.

## Development Environment 

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* I just need to import firebase_admin and sys.
* I'm using python, so setup is very simple.

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [Bro Macbeth's video](https://video.byui.edu/media/t/1_gvd1voh8)
* [W3Schools - Python] (https://www.w3schools.com/python/default.asp)
* [firebase 9 tutorial] (https://www.youtube.com/watch?v=9zdvmgGsww0&list=PL4cUxeGkcC9jERUGvbudErNCeSZHWUVlb)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [1] I want to consolidate the code, some functions use very similar code with slight differences. I would like to not have to reuse pretty much anything.
* [2] Better flow when adding a new order. Right now it asks EACH field for each order, but some fields negate other fields (i.e. if you choose chain, you don't need to specify scale color). I'll change it so it will only ask for the fields that are relevant to the order, depending on the order type.
* [3] Instead of displaying the orders as they are (the dictionary format), I want to do a more user-friendly way. I'm thinking of displaying each distinct name once, and all the orders by that customer listed below their name (maybe in a simple table, or a short bullet point list or something similar).