''''
user_text = str(input("Enter the text "))
text = user_text.split()
a = " "
for i in text:
  a=a+str(i[0].upper())
print(a)
'''


import random

min_val =1
max_val =6

rolling_dics = "Yes"
while rolling_dics == "yes" or "y" or "Yes" or "YES" :
  name = input("Enter your name ")
  print("Roling the dics..... ")
  
  print("The value are ....")
  print()
  n=random.randint(min_val , max_val)
  m=random.randint(min_val , max_val)
  print(f'This value of {name} : {n}')
  print()
  print(f'This value of computer:{m}')
  print()
  if n<m :
    print(f'kya yrr {name} tum phir haar gye ')
  else:
    print("you are win! ..")
  print()
  
  print(name  + " " " VISHUDH CHUTIYA LADKE HO TUM ")
  print()
  

  rolling_again = input("do you want rolling again...")
  

  
  
