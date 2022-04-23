#OOPS 1- CLASS (OBJECTS)
#2- METHOD
"""
BATCH17-18-CLASS
10 BACCHE (OBJECTS)
q- muJHE PATA KRNA HAII CLASS M CHL LKYA RAHA HAII AUR KON KYA KR RAHA HAII
ADITI == AS A OBJECT RETURN KR DEGI CLASS M CHL KYA RAHA HAII
"""
import pyfiglet

result = pyfiglet.figlet_format("ADITI CALCULATOR MENU BASED", font="slant")
print(result)

class Calculator:
    def __init__(self, num1,num2):
        self.number1=num1
        self.number2=num2

    def Add(self):
        result=self.number1+self.number2
        print("Adiition Of Two Number Is "+str(result))
    def Sub(self):
        result=self.number1-self.number2
        print("Subtraction Of Two Number Is "+str(result))
    def Mul(self):
        result=self.number1*self.number2
        print("Multiplication Of Two Number Is "+str(result))
    def Div(self):
        result=self.number1/self.number2
        print("Division Of Two Number Is "+str(result))

jbtakaditizerohaii=0
while(jbtakaditizerohaii==0):
    print("Enter 1 To Add")
    print("Enter 2 To Sub")
    print("Enter 3 To Mul")
    print("Enter 4 To Div")
    print("Enter 5 To Exit")
    inp=int(input("Enter Your Choice"))
    if(inp==1):
        flag = 0
        while(flag==0):
            num1 = int(input("Enter First Number"))
            num2 = int(input("Enter Second Number"))
            aditical = Calculator(num1, num2)
            aditical.Add()
            print("Enter 0 To Add Another Number Or Enter 1 To Exit")
            userinp=int(input())
            if(userinp==0):
                flag=0
            elif(userinp==1):
                flag=1
            else:
                print("Choose Correct Option")
    elif(inp==2):
        flag = 0
        while(flag==0):
            num1 = int(input("Enter First Number"))
            num2 = int(input("Enter Second Number"))
            aditical = Calculator(num1, num2)
            aditical.Sub()
            print("Enter 0 To Subtract Another Number Or Enter 1 To Exit")
            userinp=int(input())
            if(userinp==0):
                flag=0
            elif(userinp==1):
                flag=1
            else:
                print("Choose Correct Option")

    elif(inp==3):
        flag = 0
        while (flag == 0):
            num1 = int(input("Enter First Number"))
            num2 = int(input("Enter Second Number"))
            aditical = Calculator(num1, num2)
            aditical.Mul()
            print("Enter 0 To Multiply Another Number Or Enter 1 To Exit")
            userinp = int(input())
            if (userinp == 0):
                flag = 0
            elif (userinp == 1):
                flag = 1
            else:
                print("Choose Correct Option")
    elif(inp==4):
        flag = 0
        while (flag == 0):
            num1 = int(input("Enter First Number"))
            num2 = int(input("Enter Second Number"))
            aditical = Calculator(num1, num2)
            aditical.Div()
            print("Enter 0 To Divide Another Number Or Enter 1 To Exit")
            userinp = int(input())
            if (userinp == 0):
                flag = 0
            elif (userinp == 1):
                flag = 1
            else:
                print("Choose Correct Option")
    elif(inp==5):
        jbtakaditizerohaii=1
    else:
        print("Enter Correct Input")

