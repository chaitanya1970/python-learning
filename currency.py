#converting currencies after a ttip across columbia,peru,and brazil into usd and inr respectively
# this includes including datatypes,variables,input function etc
#currency converter
# exchange rates
pesos=int(input("enter the pesos left !"))
soles=int(input('enter the soles left !'))
reais=int(input('enter the reais left !'))
usd1=pesos*0.058
usd2=soles*0.30
usd3=reais*0.19
usd_total=usd1+usd2+usd3
print(usd_total)
INR=usd_total*91.08
print(INR)