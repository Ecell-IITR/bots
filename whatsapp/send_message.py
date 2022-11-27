from pyautogui import hotkey, press, typewrite 
import pandas as p
import time as t 

# t.sleep(5)
column_number=2
x=p.read_csv("CAP.csv")

# x=x.loc[:,1]
print()
# acess pandas dataframe by coulmn index
counter=1
c_name=""
for i in x:
    if counter==column_number:
        c_name=i
        break
    counter+=1
x=x.loc[:,c_name]
print("will start in 10 seconds")
t.sleep(10)
#itrate over pandas data frame
for index, row in x.iteritems():

  typewrite(str(row))
  t.sleep(1)

  press('enter')
  press('backspace')

print("completed")