class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,tracks,score):
        self.name=str(name)
        self.age=int(age)
        self.tracks=tracks
        self.score=float(score)
    def change_name(self,new_name):
        self.change_name=new_name
        print("the new student name is",new_name)

    def change_age(self,new_age):
        self.change_age=new_age
        print("the new age is",new_age)

    def add_track(self,add_track):
        self.add_track=add_track
        print("the new student track is",add_track)
    
    def get_score(self):
        return("the new student score is",self.score)
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
print(Bob.get_score())
