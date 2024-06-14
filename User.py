import json
import re
class User():
    def __init__(self,username,email,pw,level) -> None:
        self.username = username
        self.email = email
        self.password = pw
        self.level = level

    def DictUser(self):
        return{
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "level":self.level
        }
class UserData():
    def __init__(self,file) -> None:
        self.file = file
        self.users = []
        self.Read()
    def Read(self):
        try:
            with open(self.file,'r',encoding='utf-8') as file:
                self.users = json.load(file)
        except:
            pass
    def Write(self):
        with open(self.file,'w',encoding='utf-8') as file:
            json.dump(self.users, file, indent=4)
    def Add(self,newUser,repassword):   
        if not re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$',newUser["password"]):
            return 0
        elif newUser["password"] != repassword:
            return -1
        elif not re.match("[a-zA-Z0-9]+@[a-zA-z]+\.[A-Za-z]{2,}",newUser["email"]):
            return -2
        elif newUser["level"] != "Level 1" and newUser["level"] != "Level 2":
            return -3
        self.Read()     

        for user in self.users:
            if newUser["username"]  == user["username"] :
                return -4
            if  newUser["email"] == user["email"]:
                return -5
        else:            
            self.users.append(newUser)
            self.Write()
            return 1
        
    def CheckUser(self,username,password):
        self.Read()
        for user in self.users:
            if username == user["username"] and password == user["password"]:
                return user
        else:
            return 0

if __name__ == "__main__":
    s1 = User('user001','s@mail.com','matkhauA@1',"Level 1").DictUser()
    s2 = User('user002','s2@mail.com','matkhauA@1',"Level 2").DictUser()
    s3 = User('user003','s3@mail.com','12345',1).DictUser()
    a=  UserData('user.json')
    print(a.Add(s1,"matkhauA@1"))
    print(a.Add(s2,"matkhauA@1"))
