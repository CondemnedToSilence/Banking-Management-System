from validate import *

class Account():
    def __init__(self,bank_name,ifsc_code,acc_no,name,age,sex,dob,address,city,acc_type,balance,pan,aadhar,password):
        self.bank_name = bank_name
        self.ifsc_code = ifsc_code
        self.acc_no = acc_no
        self.name = name
        self.age = age
        self.sex = sex
        self.dob = dob 
        self.address = address
        self.city = city
        self.acc_type = acc_type
        self.balance = balance
        self.pan = pan
        self.aadhar = aadhar
        self.password = password
        
        
    def display(self):
        print("Bank Name: ", self.bank_name)
        print("IFSC code: ",self.ifsc_code)
        print("Account Number: ",self.acc_no)
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.sex)
        print("Date of Birth: ",self.dob)
        print("Address: ",self.address)
        print("City: ",self.city)
        print("Account Type: ",self.acc_type)
        print("Balance: ",self.balance)
        print("PAN Number: ",self.pan)
        print("Aadhar Number: ",self.aadhar)

################################################################
obj_test = Account("HDFC","ICIC0ALS987","012345678910","Manu N Prabhu","22","Male","01/10/2001","fgvjb","Chennai","Savings","12000","GACPP1234C","111122223333","password")
Account_details_dict = {}


def Security_Check(acc_no,passwd):
        while True:
            if(Account_details_dict[acc_no].password == passwd ):
                return True
            else:
                return False
                
def validate(Account_obj):
    if(not validate_BankName(Account_obj.bank_name)):
        print("Invalid Bank Name")
        return False
    if(not validate_IFSC(Account_obj.ifsc_code)):
        print("Invalid IFSC Code")
        return False
    if(not validate_AccountNo(Account_obj.acc_no)):
        print("Invalid Account Number")
        return False
    if(not validate_Name(Account_obj.name)):
        print("Invalid Name")
        return False
    if(not validate_Age(Account_obj.age)):
        print("Invalid Age")
        return False
    if(not validate_Gender(Account_obj.sex)):
        print("Invalid Gender")
        return False
    if( not validate_DOB(Account_obj.dob)):
        print("Invalid Date of Birth")
    if(not validate_City(Account_obj.city)):
        print("Invalid City")
        return False
    if(not validate_Type(Account_obj.acc_type)):
        print("Invalid Account Type")
        return False
    if(not validate_Balance(Account_obj.balance)):
        print("Invalid Balance")
        return False
    if(not validate_PAN(Account_obj.pan)):
        print("Invalid PAN")
        return False
    if(not validate_Aadhar(Account_obj.aadhar)):
        print("Invalid AAdhar")
        return False
    return True
validate(obj_test)
#################################################################
while True:
    print("Press 1 to Create Account")
    print("Press 2 to Delete Account")
    print("Press 3 to Update Account Details")
    print("Press 4 to Deposit Money")
    print("Press 5 to Withdraw Money")
    print("Press 6 for Fund Transfer")
    print("Press 7 to Search Details of Account Number")
    print("Press 8 for Balance Inquiry")
    print("Press 9 to Exit \n \n")
    
    
    usr_inp = int(input(" Please Enter Your Choice: "))
    
###################################################################    
    if(usr_inp == 1):
        d1  = input("Please Enter your Bank Name:")
        d2  = input("Please Enter your IFSC Code:")
        d3  = input("Please Enter your Account Number:")
        d4  = input("Please Enter your Name:")
        d5  = input("Please Enter your Age:")
        d6  = input("Please Enter your Gender:")
        d7  = input("Please Enter your Date of Birth(dd/mm/yyyy):")
        d8  = input("Please Enter your Address:")
        d9  = input("Please Enter your City:")
        d10 = input("Please Enter your Account Type:")
        d11 = input("Please Enter your Balance:")
        d12 = input("Please Enter your PAN Number:")
        d13 = input("Please Enter your Aadhar Number:")
        d14 = input("Please Enter your PASSWORD:")
        acc =  Account(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14)
        if(validate(acc)):
            accounts_details.append(acc)
            Account_details_dict[d3] = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14]
        
##########################################################################
    elif(usr_inp == 2):
        acc_no1 = input("Enter Account Number:")
        pwd_1 = input("Enter Password:")
        if(Security_Check(acc_no1,pwd_1)):
            Account_details_dict.pop(acc_no1)
        else:
            print("Password or Account Number is wrong. Try Again!")

#########################################################################            
    elif(usr_inp == 3):
        acc_no1 = input("Enter Account Number:")
        pwd_1 = input("Enter Password:")
        if(Security_Check(acc_no1,pwd_1)):
            while True:
                print("1 : Press 1 to Update Bank Name")
                print("2 : Press 2 to Update IFSC Code")
                print("3 : Press 3 to Update Account Number")
                print("4 : Press 4 to Update Name")
                print("5 : Press 5 to Update Age")
                print("6 : Press 6 to Update Sex")
                print("7 : Press 7 to Update D.O.B")
                print("8 : Press 8 to Update Address")
                print("9 : Press 9 to Update City")
                print("10: Press 10 to Update Account Type")
                print("11: Press 11 to Update Balance")
                print("12: Press 12 to Update PAN")
                print("13: Press 13 to Update AADHAR")
                print("14: Press 14 to Update Password")
                choice_2 = int(input("Please enter your choice:")) 
                if(choice == 1):
                    a_3 = input("Enter updated input")
                    obj_2 = Account_details_dict[acc_no1]
                    obj_2.bank_name = a_3
                    if(validate(obj_2)):
                        Account_details_dict[acc_no1].bank_name = obj_2
                    else:
                        print("Invalid Input!!")
                elif(choice == 2):
                    a_3 = input("Enter updated input")
                    obj_2 = Account_details_dict[acc_no1]
                    obj_2.ifsc_code = a_3
                    if(validate(obj_2)):
                        Account_details_dict[acc_no1] = obj_2
                    else:
                        print("Invalid Input!!")
                elif(choice == 3):
                    a_3 = input("Enter updated input")
                    obj_2 = Account_details_dict[acc_no1]
                    obj_2.acc_no = a_3
                    if(validate(obj_2)):
                        Account_details_dict[acc_no1] = obj_2
                    else:
                        print("Invalid Input!!")
                elif(choice == 4):
                    a_3 = input("Enter updated input")
                    obj_2 = Account_details_dict[acc_no1]
                    obj_2.name = a_3
                    if(validate(obj_2)):
                        Account_details_dict[acc_no1] = obj_2
                    else:
                        print("Invalid Input!!")
                elif(choice == 5):
                    a_3 = input("Enter updated input")
                    obj_2 = Account_details_dict[acc_no1]
                    obj_2.age = a_3
                    if(validate(obj_2)):
                        Account_details_dict[acc_no1] = obj_2
                    else:
                        print("Invalid Input!!")       
                elif(choice == 6):
                    a_3 = input("Enter updated input")
                    obj_2 = Account_details_dict[acc_no1]
                    obj_2.sex = a_3
                    if(validate(obj_2)):
                        Account_details_dict[acc_no1] = obj_2
                    else:
                        print("Invalid Input!!")
                elif(choice == 7):
                    a_3 = input("Enter updated input")
                    obj_2 = Account_details_dict[acc_no1]
                    obj_2.dob = a_3
                    if(validate(obj_2)):
                        Account_details_dict[acc_no1] = obj_2
                    else:
                        print("Invalid Input!!")
                        
                elif(choice == 8):
                    a_3 = input("Enter updated input")
                    obj_2 = Account_details_dict[acc_no1]
                    obj_2.address = a_3
                    if(validate(obj_2)):
                        Account_details_dict[acc_no1] = obj_2
                    else:
                        print("Invalid Input!!")
                elif(choice == 9):
                    a_3 = input("Enter updated input")
                    obj_2 = Account_details_dict[acc_no1]
                    obj_2.city = a_3
                    if(validate(obj_2)):
                        Account_details_dict[acc_no1] = obj_2
                    else:
                        print("Invalid Input!!")
                        
                elif(choice == 10):
                    a_3 = input("Enter updated input")
                    obj_2 = Account_details_dict[acc_no1]
                    obj_2.acc_type = a_3
                    if(validate(obj_2)):
                        Account_details_dict[acc_no1] = obj_2
                    else:
                        print("Invalid Input!!")
                        
                elif(choice == 11):
                    a_3 = input("Enter updated input")
                    obj_2 = Account_details_dict[acc_no1]
                    obj_2.balance = a_3
                    if(validate(obj_2)):
                        Account_details_dict[acc_no1] = obj_2
                    else:
                        print("Invalid Input!!")
                        
                elif(choice == 12):
                    a_3 = input("Enter updated input")
                    obj_2 = Account_details_dict[acc_no1]
                    obj_2.pan = a_3
                    if(validate(obj_2)):
                        Account_details_dict[acc_no1] = obj_2
                    else:
                        print("Invalid Input!!")
                        
                elif(choice == 13):
                    a_3 = input("Enter updated input")
                    obj_2 = Account_details_dict[acc_no1]
                    obj_2.aadhar = a_3
                    if(validate(obj_2)):
                        Account_details_dict[acc_no1] = obj_2
                    else:
                        print("Invalid Input!!")
                elif(choice == 14):
                    a_3 = input("Enter updated input")
                    obj_2 = Account_details_dict[acc_no1]
                    obj_2.password = a_3
                    if(validate(obj_2)):
                        Account_details_dict[acc_no1] = obj_2
                else:
                    print("Invalid Input!!")
                        
                
        else:
            print("Password or Account Number is wrong. Try Again!")

        
#####################################################################        
    elif(usr_inp == 4):
        acc_no1 = input("Enter Account Number:")
        pwd_1 = input("Enter Password:")
        if(Security_Check(acc_no1,pwd_1)):
            dep_money = int(input("Enter amount of money to deposit: "))
            if(dep_money > 0):
                Account_details_dict[acc_no1].balance = balance + dep_money
            else:
                print("Invalid Deposit amount!!")
        else:
            print("Password or Account Number is wrong. Try Again!")

        
###################################################################        
    elif(usr_inp == 5):
        acc_no1 = input("Enter Account Number:")
        pwd_1 = input("Enter Password:")
        if(Security_Check(acc_no1,pwd_1)):
            with_money = int(input("Enter amount of money to deposit: "))
            if((with_money > 0) and (Account_details_dict[acc_no1].balance > with_money)):
                Account_details_dict[acc_no1].balance = balance - dep_money
                print("Thank you for withdrawing Money!")
            else:
                print("Insufficient Balance!!")
        else:
            print("Password or Account Number is wrong. Try Again!")
###################################################################        
    elif(usr_inp == 6):
        acc_no1 = input("Enter Your Account Number:")
        pwd_1 = input("Enter Password:")
        if(Security_Check(acc_no1,pwd_1)):
            acc_no2 = input("Enter the recipient Account Number:")
            if(acc_no2 in Account_details_dict.keys()):
                transfer_amount = int(input("Enter amount to transfer:"))
                if((transfer_amount> 0) and (Account_details_dict[acc_no1].balance > transfer_amount)):
                    Account_details_dict[acc_no1].balance = balance - dep_money
                    Account_details_dict[acc_no2].balance = balance + dep_money
                    print("TYour Fund Transfer was Successful")
                else:
                    print("Insufficient Balance!!")
            else:
                print("Invalid Recipient Address!!")
        else:
            print("Password or Account Number is wrong. Try Again!")
###################################################################        
    elif(usr_inp == 7):
        while True:
            print("1. Press 1 to search by Account Number")
            print("2. Press 2 to search by Name")
            print("3. Press 3 to search by Accont Type")
            print("4. Press any other Button to Exit")
            choice = int(input("Enter your choice"))
            
            #######################################################
            if(choice == 1):
                acc_no1 = input("Enter account number:")
                if(acc_no1 in Account_details_dict.keys()):
                    Account_details_dict[acc_no1].display()
                    break
                else:
                    print("Invalid Accont Number")
                    
            #######################################################      
            elif(choice == 2):
                name_1 = input("Enter name:")
                flag = True
                for k,v in Account_details_dict:
                    if(v.name == name_1):
                        flag = False
                        v.display()
                        break
                if(flag):
                    print("Name not Found")
                    
                    
            #######################################################
            elif(choice == 3):
                acc_type_1 = input("Enter the account type:")
                for k,v in Account_details_dict:
                    if(v.acc_type == acc_type_1):
                        flag = False
                        v.display()
                        break
                if(flag):
                    print("Records not Found")
            #######################################################
            else:
                break
            
###################################################################        
    elif(usr_inp == 8):
        acc_no1 = input("Enter Account Number:")
        pwd_1 = input("Enter Password:")
        if(Security_Check(acc_no1,pwd_1)):
             print("Balance is:", Account_details_dict[acc_no1].balance)
        else:
            print("Password or Account Number is wrong. Try Again!")

 ###################################################################       
    elif(usr_inp == 9):
        print("Thank you for using our bank!")
        break
###################################################################
    else:
        print("Invalid Input \n")
        
    
