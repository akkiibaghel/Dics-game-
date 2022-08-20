import random

min_val =1
max_val =6

rolling_dics = "Yes"
while rolling_dics == "yes" or "y" or "Yes" or "YES" :
  name = input("Enter your name ")
  print("Roling the dics..... ")
  
  print("The value are ....\n")
  print()
  n=random.randint(min_val , max_val)
  m=random.randint(min_val , max_val)
  print(f'This value of {name} : {n}\n')
  
  print(f'This value of computer:{m}\n')
  
  if n<m :
    print(f'kya yrr {name} tum phir haar gye ')
  else:
    print("you are win! ..\n")
  
  
  print(name  + " " " VISHUDH CHUTIYA LADKE HO TUM \n")

  

  rolling_again = input("do you want rolling again...")
  

  
  
