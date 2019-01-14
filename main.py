
# if the class does not subclass, you do not need :
# Our base class; no parents needed in definition

class Animal:
    def __init__(self, species, leg_num=0, domesticated=False):
        self.species = species
        self.leg_num = leg_num
        self.domesticated = domesticated

    def saySomething(self):
        if self.species == "dog":
            return "woof"
        if self.species == "cat":
          return "meow"
        else:
            return "Go fuck yourself human"

    def __str__(self):
        return f"This Animal is a {self.species} with {self.leg_num} legs and that says {self.saySomething()}"

if __name__ == "__main__":
    dog = Animal("dog", 4, True)
    cat = Animal("cat", 4, True)
    print(dog)
    print(cat)


class Dog(Animal):
    def __init__(self, breed):
        self.breed = breed
        super().__init__("dog", leg_num=4, domesticated=True)

    def speak(self):
        return f"I am a dog, so I say {self.saySomething()}"


class Pet:
    def __init__(self, name, critter_instance):
        self.name = name
        self.animal_type = critter_instance

    def set_owner(self, name, phone): 
        self.owner_name = name
        self.owner_number = phone

    def __str__(self):
        return f'This pet\'s name is {self.name}. It has {self.animal_type.leg_num} legs and it likes to say {self.animal_type.saySomething()}!'

aussie_mix = Dog("Aussie/Border Collie mix")
merch = Pet("Tobias", aussie_mix)
merch.set_owner("The Wood", "555-555-5555")


print(merch)




    

