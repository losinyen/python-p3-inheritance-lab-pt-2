class Student:
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")
        

    def raise_hand(self):
        print("Pick me!")
        
    pass

class ChattyStudent(Student):
    def hello(self):
        super().hello()
        print("How are you doing today? \n I'm okay, but I'm kind of tired.\n Did you watch, The Walking Dead last night? \n You didn't?! Oh man, \n it was so crazy! \n What you don't want any spoilers? Okay well let me just tell you who died...")
        
    def raise_hand(self):
        for x in range(0,10):
         super().raise_hand()
        
              
    pass
trin = Student()
sam = ChattyStudent()
trin.hello()
sam.raise_hand()