### Conceptual Exercise

Answer the following questions below:

-  What are important differences between Python and JavaScript?

   -  Python is a backend language that is designed to interface with data, as opposed to JavaScript which is frequently a middle ground between the data back end and the html-based front end.

-  Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you
   can try to get a missing key (like "c") _without_ your programming
   crashing.

   -  I would use the `dictionary.get('c')`. You could also use `dictionary['c']` ut that would raise an error.

-  What is a unit test?

   -  A unit test tests one particular function or method. eg: `a + b == 2`

-  What is an integration test?

   -  An integration test tests how functions should work together, eg: the right variables are being sent from one function to another and everything is working together

-  What is the role of web application framework, like Flask?

   -  The framework like Flask helps to organize and structure an entire set of web pages that work together, along with the back end. Flask provides for page templates and routing so that the developer can insert variables, return status codes, etc.

-  You can pass information to Flask either as a parameter in a route URL
   (like '/foods/pretzel') or using a URL query param (like
   'foods?type=pretzel'). How might you choose which one is a better fit
   for an application?

   -  A URL query parameter often comes from a form, and it feels less like the **main subject** of the page.

-  How do you collect data from a URL placeholder parameter using Flask?

   -  Data from a URL placeholder is retrieved using carrot bracketsin the URL and then pass the variable name into the view function as well
      -  `@app.route('user/<username>')`
      -  `def show_user_profile(username)`

-  How do you collect data from the query string using Flask?

   -  Data from the query string is found in the `request.args` dictionary-like-thing.

-  How do you collect data from the body of the request using Flask?

   -  Data from the body of the request is found in `request.form`

-  What is a cookie and what kinds of things are they commonly used for?

   -  A cookie is a piece of data that your browser saves until it expires. Cookies are often used for stuff like session time, logged in-ness, shopping cart iinfo, etc.

-  What is the session object in Flask?

   -  the Session Object is Flask's way of storing cookies. These are encrypted and not user editable.

-  What does Flask's `jsonify()` do?
   -  `jsonify()` converts a Flask response into json for you :)
