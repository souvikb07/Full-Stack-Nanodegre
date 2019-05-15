class Parent():
    def __init__(self, lastname, eyecolor):
        print("Parent Constructor Called")
        self.last_name = lastname
        self.eye_color = eyecolor
    def show_info(self):
        print(self.last_name + " : Last Name")
        print(self.eye_color + " : Eye Color")
# create child inheritance class
class Child(Parent):
    def __init__(self, lastname, eyecolor, numberoftoys):
        print("Child Constructor Called")
        Parent.__init__(self, lastname, eyecolor)
        self.toys = numberoftoys
    #this function is written to override the show info function
    def show_info(self):
        print(self.last_name + " : Last Name")
        print(self.eye_color + " : Eye Color")
        print(str(self.toys) + " : Number of Toys")
#par = Parent("banerjee", "black")
#print(par.last_name)
chil = Child("Banerjee", "Blue", 5)
print(chil.last_name)
print(chil.toys) 
chil.show_info()
