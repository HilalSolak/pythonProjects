import time
import datetime
print("3")
time.sleep(0.5)
print("2")
time.sleep(0.5)
print("1")
time.sleep(0.5)
zaman=datetime.datetime.now()

n=str(input("yazı giriniz: "))
zaman1=datetime.datetime.now()
hiz=zaman1-zaman
sure=round(hiz.total_seconds(),2)
print(sure," saniyede yazdınız")