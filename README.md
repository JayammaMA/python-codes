# python-codes

/*simple python programs*/
import re
def validate_pw(pwd):
  if len(pwd)<=8:
   print("min.8 character are allowed")
   return False
  if not re.search("[a-z]",pwd):
   print("min 1 lowercase character required");
   return False
  if not re.search("[A-Z]",pwd):
   print("min 1 uppercase character required");
   return False
  if not re.search("[0-9]",pwd):
   print("min 1 number is required");
   return False 
   if not re.search("[$@#]",pwd):
   print("min 1 special symbol is required");
   return False
  return True
  pwd=input("enter your password")
  if(validate_pw(pwd)):
     print("valide password")
  else
    print("invalide password")
    
   
