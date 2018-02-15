####################################
#  Python Login Validation System  #
#        By coolhobo77             #
####################################

# This module aims to provide a clear layout for a login system based in Python
# This module is not over-complicated and very straightforward to use!
# This is a way for beginners to look into modules and see how they work

# Defines an Array that Contains Every Instantiated User Class added
totalUsers = []

# User Class that Provides the Structure for a User Object
# This class is what is created on invoking the createUser() function
class User:

    # User Class Constructor, Defines Variable Names in a Global Reach within the Class Object
    # Also appends the Object to the __totalUsers array on it's creation
    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        totalUsers.append(self)

    # Returns all info about a given user object
    def getInfo(self):
        print(self.name)
        print(self.surname)
        print(self.email)
        print(self.password)

    # Returns the Password of a Certain User
    def getPassword(self):
        return self.password

# Returns a new instantiation of the User Class for storage in a variable
# Instantiations can be accessed later by accessing the __totalUsers array
def createUser(name, surname, email, password):
    return User(name, surname, email, password)

# Returns a new instantiation of the User Class based off of user inputs
# Will return the User if the entries are valid, but will return False if they are not
def inputUser(nameEntry, surnameEntry, emailEntry, passwordEntry):
    name = str(input(nameEntry + " : "))
    surname = str(input(surnameEntry + " : "))
    email = str(input(emailEntry + " : "))
    password = str(input(passwordEntry + " : "))
    if(validateInputs(name, surname, email, password)):
        return createUser(name, surname, email, password)
    else:
        return False


# Validates the password of a specific user against a preset password
# This will return true if the password is valid and False if it is not
def validateUser(user, password):
    if(user.password == password):
        return True
    else:
        return False

#Lists all Users inside the __totalUsers array
def listUsers():
    safeUsers = []
    for user in totalUsers:
        safeUsers.append({user.name, user.surname, user.email})
    return safeUsers

# Checks all the Users to see if a password and email match is found
# This will return True if a match is found, and False if not
def userExists(email, password):
    for user in totalUsers:
        if(user.email == email and user.password == password):
            return True
        else:
            return False
