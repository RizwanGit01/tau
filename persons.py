import random


class Person:
    def __init__(self, firstname, lastname, health, status):
        ''' Initialize attributes to be used in/available for all \
        class methods in this class, and for class objects created \
        by this class.'''

        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        "All people introduce themselves"
        print("Hello my name is {} {}".format(self.firstname, self.lastname))

    def emote(self):
        emotion = random.randrange(1,3)
        if emotion == 1:
            print("{} is happy today".format(self.firstname))
        elif emotion == 2:
            print("{} is sad right now".format(self.lastname))

    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy".format(self.firstname))
        elif self.health >= 70:
            print("{} feels little tired today".format(self.firstname))
        elif self.health >= 51:
            print("{} feels unwell".format(self.firstname))
        elif self.health >= 40:
            print("{} goes to the doctor".format(self.firstname))
        else:
            print("{} is unconscious.".format(self.firstname))

Maria = Person("Maria", "Geron", 75, status=True)
Rey = Person("Rey", "John", 65, status=False)
Lee = Person("Lee", "William", 45, status=True)

print("{} is my Friend? {}".format(Maria.firstname, Maria.status))
print("{} is my Friend? {}".format(Rey.firstname, Rey.status))

Maria.introduce()
Rey.introduce()
Lee.introduce()

Maria.status_change()
Rey.status_change()
Lee.status_change()


class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        self.weapon = weapon

    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -= 5
        print(other.health)
    
    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and weak".format(other))