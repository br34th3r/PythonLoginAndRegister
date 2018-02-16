# Python Login And Register
Basic Login and Registration System to be Used by New Developers to Structure their own Modules

## Contents
* Introduction
* Documentation
* Examples
* Installation

## Introduction
_Python Login and Register_ is a module developed to provide basic user authentication in Python. It is a very bare-bones structure for the reason that other developers can access the contents of the source files and look around in order to learn how to structure their own modules or projects. Furthermore, the module provides a quick access to check user validation through comparison with another Python variable or direct string value, and a developer can easily use the in-built functions to create a user registration system. Python Login and Register can only be used to regsiter users with the following information:

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

This function will return True or False respectively depending on the value. This is a search through the whole array for a specific user to see if they exist or not and could be used to validate logins, however a second check should be run to make sure this is not a form of bruteforcing

#### Validate User
A User can be validated at any point in the code quite easily to see if their password matches a prescribed standard password that the developer invokes.

```python
  # Validate an Existing User
  validateUser(UserObject, "PASSWORD")
```

Unlike User Eistance, User Validation uses a preset password and only requires the single user object to validate. This means that the system does not have to browse an entire array for a user to validate, when the user information is stored on a local object

### User Removal
A user can simply be removed from an array by calling the following function with their email as the parameter :

```python
  # Remove a Specific User
  removeUser("EMAIL")
```

## Examples
The following examples can be used to show basic functionality of the system

### Basic Login

```python
  email = str(input("Enter Your Email : "))
  password = str(input("Enter Your Password : "))
  
  if userExists(email, password):
      print("Welcome!")
  else:
      print("Sorry, Invalid Credentials!")
```

### Basic Registration (Without Registration Function)

```python
  name = str(input("Enter Your Name : "))
  surname = str(input("Enter Your Surname : "))
  email = str(input("Enter Your Email : "))
  password = str(input("Enter Your Password : "))
  confPassword = str(input("Confirm Your Password : "))
  
  if(password == confPassword):
      print("User Accepted!")
      user = createUser(name, surname, email, password)
  else:
      print("User Rejected! Invalid Password Combination")
```

_Conditionals can be used to create more validation methods, functions are planned to be implemented in the near future_

### Basic Registration (With Registration Function)

```python
  user = inputUser("Enter Your First Name : ", "Enter Your Surname : ", "Enter Your Email : ", "Enter Your Intended Password : ")
```

### Stored Password Check

```python
  user = createUser("Josh", "Jameson", "joshywashy1@spaceymail.com", "MIDAS")
  adminPassword = "MIDAS"
  
  if validateUser(user, adminPassword):
      print("You have Admin Access!")
  else:
      print("You Don't Have Admin Access!")
```

_Please don't use this code, it's very insecure and any user that sets their password as MIDAS will have admin access!_
_Demonstration Purposes Only!_

### Remove a User from the System

```python
  user = createUser("Josh", "Jameson", "joshywashy1@spaceymail.com", "MIDAS")
  
  if validateUser(user, "ZEUS") != True:
      removeUser(user.email)
  else:
      print("Welcome!")
```

## Installation
Python setup.py installation :

```bash
  python setup.py install
```

or use pip :

```bash
  pip install PythonLoginAndRegister
```

## More Info
[Python Login and Register on GitHub](https://github.com/kamohoaliix/PythonLoginAndRegister/)

[Kamohoaliix on GitHub Pages](https://kamohoaliix.github.io/)
