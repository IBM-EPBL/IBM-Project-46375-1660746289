import random
i=1

while(i<=7):
  a=random.randint(20,200)  
  b=random.randint(20,100)  
  print(f'Day {i}') 
  print(f'Temperature:{a}')
  print(f'Humidity   :{b}')
  if a>80:
    if b>80:
      print("Hazard Predicted...")
    else:
      print("Temparature is high!!! ")
  elif a==80:
    print("Average Temperature Reached ")
  else:
    print("No issues found")
  i=i+1
  print(end="\n")