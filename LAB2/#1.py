users=set()
purchases=0
sales=0
spendings={}
data="""2026-02-01;user_1;LOGIN
2026-02-01;user_2;LOGIN
2026-02-01;user_1;BUY;120
2026-02-01;user_3;LOGIN
2026-02-01;user_2;BUY;300
2026-02-01;user_1;BUY;50
2026-02-01;user_2;LOGOUT"""
with open('shop_log.txt','w', encoding='utf-8') as file:
    file.write(data)
with open('shop_log.txt',"r",encoding='utf-8') as file:
    for line in file:
        parts = line.strip().split(';')
        if not parts or parts ==['']:
            continue
        date = parts[0]
        id = parts[1]
        action = parts[2]
    users.add(id)
    if action == "BUY":
        amount=int(parts[3])
        purchases+=1
        sales+= amount
    if id in spendings:
        spendings[id]+=amount
    else:
        spendings[id]=amount
max_spent = 0
top_buyer = ""
for id, total_amount in spendings.items():
    if total_amount > max_spent:
        max_spent = total_amount
        top_buyer = id
average=sales / purchases
with open('report.txt', 'w', encoding='utf-8') as report:
    report.write(f"Уникальных пользователей: {len(users)}\n")
    report.write(f"Всего покупок: {purchases}\n")
    report.write(f"Общая сумма: {sales}\n")
    report.write(f"Самый активный покупатель: {top_buyer}\n")
    report.write(f"Средний чек: {average:.2f}\n")
print("Отчет успешно создан в файле report.txt")