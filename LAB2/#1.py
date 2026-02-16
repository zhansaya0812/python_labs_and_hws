
users=set()
purchases=0
sales=0
spendings={}
data="""
2026-02-01;user_1;LOGIN
2026-02-01;user_2;LOGIN
2026-02-01;user_1;BUY;120
2026-02-01;user_3;LOGIN
2026-02-01;user_2;BUY;300
2026-02-01;user_1;BUY;50
2026-02-01;user_2;LOGOUT"""
with open('shop_log.txt','w', encoding='utf-8') as file:
    file.write(data)
with (open('shop_log.txt',"r",encoding='utf-8') as file):
    for line in file:
        line = line.strip()
        if not line:
            continue
        parts = line.split(';')
        date = parts[0]
        user_id = parts[1]
        action = parts[2]
        users.add(user_id)
        if action == "BUY":
            amount=int(parts[3])
            purchases+=1
            sales += amount
            if user_id in spendings:
                spendings[user_id]+=amount
            else:
                spendings[user_id] = amount
top_user = ""
max_spent=0
for user in spendings:
    if spendings[user] > max_spent:
        max_spent = spendings[user]
        top_user = user
average=0
if purchases > 0:
    average=sales / purchases
with open('report.txt', 'w', encoding='utf-8') as report:
    report.write(f"Уникальных пользователей: {len(users)}\n")
    report.write(f"Всего покупок: {purchases}\n")
    report.write(f"Общая сумма: {sales}\n")
    report.write(f"Самый активный покупатель: {top_user}\n")
    report.write(f"Средний чек: {average:.2f}\n")