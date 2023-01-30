import pywhatkit as pwk
import pandas as pd
# df = pd.read_csv('vdc.csv',usecols =['PhoneNo'])
df=["+919690081422","+919833290022","+919548458597"]
hrs= int(input("hrs - "))
Min = int(input(" Min - "))
count=0;set=0
for i in df:
 print(i)
 try:
     print(i)
     pwk.sendwhatmsg(i, "Hi, how are you?",hrs+(Min+count)//60,(Min+count)%60 )
 
     print("Message Sent!") 
 except: 
     print("Error in sending the message")

 count+=1
