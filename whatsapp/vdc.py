# python function to store multiple contacts in vcards
def make_vcard(
        first_name="",
        last_name="",
        company="CAP",
        title="",
        phone="",
        address="",
        email=""):
    address_formatted = ';'.join([p.strip() for p in address.split(',')])
    return [
        'BEGIN:VCARD',
        'VERSION:2.1',
        f'N:{last_name};{first_name}',
        f'FN:{first_name} {last_name}',
        f'ORG:{company}',
        f'TITLE:{title}',
        f'EMAIL;PREF;INTERNET:{email}',
        f'TEL;WORK;VOICE:{phone}',
        f'ADR;WORK;PREF:;;{address_formatted}',
        f'REV:1',
        'END:VCARD'
    ]
import time as t 
import pandas as p
# t.sleep(5)
column_number=2
x=p.read_csv("CAPg.csv")

# x=x.loc[:,1]
print()
# acess pandas dataframe by coulmn index
counter=1
print(x.loc[:,:])
#itrate over pandas data frame
f=open("contacts.vcf","w")
for row in x.loc[:,:].itertuples():
  print(row[2],row[3],row[0])
  mc=make_vcard(first_name=row[3],phone=row[2],email=row[1])
  f.writelines([l + '\n' for l in mc])
  f.write("\n")
  pass
f.close()
print("completed")