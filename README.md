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
  person = createUser("NAME", "SURNAME", "EMAIL", "PASSWORD)
  
  # Option 2
  person = User("NAME", "SURNAME", "EMAIL", "PASSWORD")
```

Furthermore, the module comes with an in-built entry form to create a user. This can be used in the command line and one can customise the input message for the input and so could be used by administrators to quickly create users. This is done with the following function :

```python
  # Input New User with a Form
  person = inputUser("NAME ENTRY PROMPT", "SURNAME ENTRY PROMPT", "EMAIL ENTRY PROMPT", "PASSWORD ENTRY PROMPT")
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

### List Users
There are two options currently to list the current users. One 'safe' way and one 'unsafe' way. These are as follows :

```python
  # List All Users Without Displaying Passwords (safe)
  listUsers()
  
  # List All Users While Displaying Passwords (unsafe)
  unsafeList()
```

The unsafe listing of users will require an admin with access to the terminal to confirm the listing of the users in an 'unsafe' fashion

### User Validation
#### User Existance
A user can be checked to see if their object exists using the following function :

```python
  # Check if a User Exists
  userExists("EMAIL", "PASSWORD")
```

This function will return True or False respectively depending on the value.
