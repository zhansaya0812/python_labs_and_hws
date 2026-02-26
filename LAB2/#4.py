import csv
import json
users_count={}
suspicious_users=set()
suspicious_operations=[]
total_s_operations=0
transactions="""user_id,amount

user_1,5000

user_2,10000

user_1,700000

user_3,3000

user_2,900000

user_4,2000"""
with open('transactions.csv', 'w',encoding='utf-8') as file:
    file.write(transactions)
with open('transactions.csv', 'r') as file:
    transaction = csv.DictReader(file)
    for row in transaction:
        user = row['user_id']
        amount =int(row['amount'])
        users_count[user]=users_count.get(user,0)+1
        if amount>500000:
            suspicious_operations.append(amount)
            total_s_operations+=amount
            suspicious_users.add(user)
for user,count in users_count.items():
    if count>3:
        suspicious_users.add(user)
with open('report.txt', 'w',encoding='utf-8') as file:
    file.write("Подозрительных транзакций:"+str(len(suspicious_operations))+"\n")
    file.write("Подозрительных пользователей:"+str(len(suspicious_users))+"\n")
    file.write("Список пользователей:"+str(', '.join(suspicious_users))+ "\n")
    file.write("Общая сумма подозрительных операций:"+str(total_s_operations)+"\n")
with open('susp_users.json', 'w', encoding='utf-8') as file:
    json.dump(list(suspicious_users), file,indent=4,ensure_ascii=False)
print("json file is ready")