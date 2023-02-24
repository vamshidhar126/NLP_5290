import tags
import currency
import date
import phonenumber

input = open('input.txt','r',encoding='utf-8')
for x in input:
    print(x)
    if not tags.isTag(x):
        phonenumber.isValidphn(x)
        currency.isValidcurr(x)
        date.isValidDate(x)