import csv
employees=[]
departments={}
data="""name,department,salary

Ali,IT,500000

Dana,HR,300000

Arman,IT,600000

Aruzhan,Marketing,400000

Dias,IT,450000"""
with open("employees.csv","w",encoding="utf-8") as f:
    f.write(data)
with open("employees.csv","r",encoding="utf-8") as f:
    reader = csv.DictReader(f)
    salary_sum=0
    for row in reader:
        name=row['name']
        dep=row['department']
        salary=int(row['salary'])
        info={'name':name,'department':dep,'salary':salary}
        employees.append(info)
        salary_sum+=salary
        if dep not in departments:
            departments[dep]=[0,0]
        departments[dep][0]+=salary
        departments[dep][1]+=1
count=len(employees)
if count>0:
    average=salary_sum/count
else:
    average=0
average_d=0
best_department=0
for d in departments:
    sum_=departments[d][0]
    count_=departments[d][1]
    if count_>0:
        current_average_d=sum_/count_
    else:
        current_average_d=0
    print(f"{d}:{current_average_d:.2f}")
    if current_average_d > average_d:
        average_d=current_average_d
        best_department=d
best_employee=employees[0]
avg_employees=[]
for emp in employees:
    if emp['salary']>=best_employee['salary']:
        best_employee=emp
    if emp['salary']>average:
        avg_employees.append(emp)
print("Общая средняя зарплата:"+str(average)+"\n")
print("Отдел с самой высокой средней зарплатой:"+str(best_department)+"\n")
print("Самый высокооплачиваемый сотрудник:"+str(best_employee['name'])+" - "+ str(best_employee['salary'])+"\n")
with open('high_salary.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'department', 'salary'])
    writer.writeheader()
    writer.writerows(avg_employees)