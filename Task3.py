import json
from datetime import datetime

with open('operations.json', 'r', encoding='utf-8') as f:
    file = json.load(f)

data = []
for i in file:
    try:
        if i["state"] == 'EXECUTED':
            data.append(i)
    except KeyError:
        pass

data_sorted = sorted(data, key=lambda x: (x['date']), reverse=True)


def hide_number(account):
    account_number = account.split(' ')[-1]
    if len(account_number) == 20:
        return f'Счёт **{account_number[16:]}'
    else:
        return f'{" ".join(account.split(" ")[:-1])}' \
               f'{account_number[0:4]} {account_number[4:6]}' \
               f'** **** {account_number[12:]}'

res_lst = []
for i in data_sorted:

    try:
        a = hide_number(i["from"])
        b = hide_number(i["to"])
        date = datetime.strptime(i['date'][0:10], '%Y-%m-%d').strftime("%d.%m.%Y")
        desc = i['description']
        sum = i["operationAmount"]["amount"]
        currency = i["operationAmount"]["currency"]["name"]
        res_lst.append(f'{date} {desc}\n{a} -> {b} \n{sum} {currency}\n')

    except KeyError:
        pass

count = 5
for i in res_lst:
    print(i)
    count -= 1
    if count == 0:
         break
