# Python Login And Register
Basic Login and Registration System to be Used by New Developers to Structure their own Modules

## Contents
* Introduction
* How to Use
* Documentation
* Installation

## Introduction
_Python Login and Register_ is a module developed by coolhobo77 to provide basic user authentication in Python. It is a very bare-bones structure for the reason that other developers can access the contents of the source files and look around in order to learn how to structure their own modules or projects. Furthermore, the module provides a quick access to check user validation through comparison with another Python variable or direct string value, and a developer can easily use the in-built functions to create a user registration system. Python Login and Register can only be used to regsiter users with the following information:

  * Name
  * Surname
  * Email
  * Password

_Refer to the documentation section for specific information on what methods can be called to interact with Users and add information_

## How to Use
### Create a User
The creation of a user is quite simple and has two options, you can use either of the following methods :

```python
  # Option 1
  person1 = createUser("NAME", "SURNAME", "EMAIL", "PASSWORD)
  
  # Option 2
  person1 = User("NAME", "SURNAME", "EMAIL", "PASSWORD")
```

### User Properties
The User object now has some accessible properties. These are the name, surname, email and password properties. These can be called as variables to the object like so :

```python
  # Call User Information
  person1.name
  person1.surname
  person1.email
  person1.password
```
