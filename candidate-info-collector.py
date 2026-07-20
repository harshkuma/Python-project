class interview_candidate:
    
    def __init__(self):
        self.name = ''
        self.age = 0
        self.college = ''
        self.course = ''
        self.location = ''
        self.member = 0
        self.email = ''
        
    def ask(self, message):
        value = input(message)
        return value
    
    def general(self):
        self.name = self.ask("name: ")
        
        while True:
            try:
                self.age = int(self.ask("age: "))
                break
            except:
                print("!!!Enter a valid input!!!")
                print()
                
        self.college = self.ask("college: ")
        self.course = self.ask("course: ")
        
        while True:
            try:
                self.member = int(self.ask("total family member: "))
                break
            except:
                print("!!!Enter a valid input!!!")
                print()
                
        self.email = self.ask("email: ")
    
    def address(self):
        self.location = self.ask("Location: ")
    
    def display(self):
        print()
        print("Here are the details of the candidate:")
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"college: {self.college}")
        print(f"course: {self.course}")
        print(f"family member: {self.member}")
        print(f"email: {self.email}")
        print(f"location: {self.location}")
        self.edit_option()
        
            
        
    def edit_option(self):
        print()
        self.choice = input("Would you like to edit any field (y/n): ")
        
        if self.choice.lower() =='y':
            print('1.name')
            print('2.age')
            print('3.college')
            print('4.course')
            print('5.member')
            print('6.email')
            print('7.location')
            self.ask_again()
            
            
        elif self.choice.lower()=='n':
            print("Details saving....")
            print()
        
        else:
            print("!!!Invalid input!!!")
            self.edit_option()
            
    def ask_again(self):
        while True:
            try:
                print()
                self.asking = int(input("Enter field number you like to edit: "))
                break
            except:
                print("!!!Enter a valid input!!!")
        self.edit_input()
                
    def edit_input(self):
        print()
        if self.asking ==1:
            self.name = self.ask("name: ")
            self.display()

        elif self.asking ==2:
            while True:
                try:
                    self.age = int(self.ask("age: "))
                    break
                except:
                    print("!!!Enter a valid input!!!")
                
            self.display()

        elif self.asking ==3:
            self.college = self.ask("college: ")
            self.display()

        elif self.asking ==4:
            self.course = self.ask("course: ")
            self.display()

        elif self.asking ==7:
            self.location = self.ask("location: ")
            self.display()

        elif self.asking ==5:
            while True:
                try:
                    self.member = int(self.ask("total family member: "))
                    break
                except:
                    print("!!!Enter a valid input!!!")
            self.display()

        elif self.asking ==6:
            self.email = self.ask("email: ")
            self.display()
            
            
        else:
            print("!!!Invalid input!!!")
            print()
            self.ask_again()
            
    def save_data(self):
        file = open("candidate_details.csv", "a")
        file.write(f"{self.name},{self.age},{self.college},{self.course},{self.location},{self.member},{self.email}\n")
        file.close()
        

        
def main():
    while True:
        candidate = interview_candidate()
        candidate.general()
        candidate.address()
        candidate.display()
        candidate.save_data()
        
        while True:
            choice = input("Would you like to enter another candidate detail (y/n): ")
            if choice == "y":
                print()
                break
            
            elif choice == 'n':
                print("All details saved successfully.")
                return
            else:
                print("!!!Invalid Input!!!")
    



    
if __name__ =='__main__':
    main()