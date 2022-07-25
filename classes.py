# classes are like blueprints for creating objects. An object has properties and methods (functions) associated
# with it. Almost everything in python is an object

class user:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# Extending class


# To intialize user object
#ife = user('seyi', 'seyi@gmail.com', 37)

#print(ife.name, ife.age, ife.email)
