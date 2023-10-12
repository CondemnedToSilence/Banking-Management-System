def validate_BankName(a):
    bank_names = ('HDFC', 'ICICI', 'HSBC', 'Standard Charted', 'IFSC')
    if(a in bank_names):
        return True
    else:
        return False
    
def validate_IFSC(a):
    if((len(a) == 11) and (a[0:4].isupper()) and (a[4] == '0') and (a[5:].isalnum())):
        return True
    else:
        return False
    
def validate_AccountNo(a):
    if((len(a)>10) and (len(a) < 18) and a.isnumeric()):
        return True
    else:
        return False
        
def validate_Name(a):
    if((len(a.split(' ')) <= 3) and a.istitle()):
        return True
    else:
        return False

def validate_Age(a):
    if(a.isnumeric() and (int(a) >10)):
        return True
    else:
        return False
def validate_Gender(a):
    b = ("Male","Female","Other")
    if(a in b):
        return True
    else:
        return False
        
def validate_DOB(a):
    #dd\mm\yyyy
    days_31 = [1,3,5,7,8,10,12]
    days_30 = [4,6,9,11]
    b  = a.split('/')
    if((int(b[1]) >= 1) and (int(b[1]) <=12) and (b[2].isnumeric) and (int(b[2]) > 0) and (int(b[0])>0)): 
        if(((int(b[1]) in days_31 )and (int(b[0])<=31))  or  (int(b[1]) in days_30 and (int(b[0])<=30))  or ((int(b[1]) == 2) and (int(b[0]) < 29))):
            return True
    else:
        return False
        

def validate_email(a):
    b = a.split('@')
    if((len(b) == 2) and (b[0].isalnum()) and (not b[0].isnumeric) and ('.' in b[2])):
        return True
    else:
        return False
        
def validate_phone_num(a):
    if(a.isnumeric()  and  (len(a) == 10)):
        return True
    else:
        return False
    
def validate_City(a):
    b = ('Chennai', 'Pune', 'Gurgaon')
    if(a in b):
        return True
    else:
        return False
def validate_Type(a):
    b = ('Savings', 'Salary', '')
    if(a in b):
        return True
    else:
        return False
def validate_Balance(a):
    if(a.isnumeric() and (int(a) > 0)):
        return True
    else:
        return False
def validate_PAN(a):
    if(a[0:5].isalpha() and a[5:9].isnumeric() and a[9].isalpha() and a.isupper() and (len(a) == 10)):
        return True
    else:
        return False
def validate_Aadhar(a):
    if((a.isnumeric()) and (len(a) == 12)):
        return True
    else:
        return False


    
    
