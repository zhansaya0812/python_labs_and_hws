import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = BASE_DIR + '\\'


#ЗАДАЧА 1
print("ЗАДАЧА 1 — Загрузка и первичный обзор")

import os
import pandas as pd

# Автоматически берёт папку, где лежит скрипт
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(BASE_DIR, 'hospital_patient_treatment.xlsx')

df = pd.read_excel(file)
df.to_csv(os.path.join(BASE_DIR, 'hospital_patient_treatment.csv'), index=False)
df = pd.read_csv(os.path.join(BASE_DIR, 'hospital_patient_treatment.csv'), encoding='utf-8')

print("\nПервые 10 строк:")
print(df.head(10).to_string())

print("\nКоличество пациентов по Department:")
print(df['Department'].value_counts().to_string())

print("\nКоличество пациентов по Treatment_Type:")
print(df['Treatment_Type'].value_counts().to_string())

print("\nСредний Treatment_Cost:", round(df['Treatment_Cost'].mean(), 2))
print("Медианный Treatment_Cost:", round(df['Treatment_Cost'].median(), 2))
print("Средний Days_in_Hospital:", round(df['Days_in_Hospital'].mean(), 2))
print("Медианный Days_in_Hospital:", round(df['Days_in_Hospital'].median(), 2))
print("Средний Lab_Test_Count:", round(df['Lab_Test_Count'].mean(), 2))
print("Медианный Lab_Test_Count:", round(df['Lab_Test_Count'].median(), 2))

#ЗАДАЧА 2
print("ЗАДАЧА 2 — Работа со строками и списками")

long_ids = [pid for pid in df['Patient_ID'] if len(pid) > 8]
print(f"\nPatient_ID длиной > 8 символов (первые 10): {long_ids[:10]}")
print(f"Всего таких ID: {len(long_ids)}")

departments_upper = [dep.upper() for dep in df['Department'].unique()]
print(f"\nОтделения в верхнем регистре: {departments_upper}")

cardiology_avg_age = df[df['Department'].str.upper() == 'CARDIOLOGY']['Age'].mean()
print(f"\nСредний возраст пациентов в CARDIOLOGY: {round(cardiology_avg_age, 2)}")


#ЗАДАЧА 3
print("ЗАДАЧА 3 — Фильтрация и генератор")

def premium_patients(dataframe):
    for _, row in dataframe.iterrows():
        if row['Treatment_Cost'] >= 30000 and (row['Lab_Test_Count'] + row['Medication_Count']) >= 20:
            yield row

gen = premium_patients(df)
print("\nПервые 15 premium-пациентов (Treatment_Cost >= 30000, Lab+Med >= 20):")
print(f"{'Patient_ID':<15} {'Treatment_Cost':>15} {'Lab+Med':>10}")
print("-" * 43)
for i, row in enumerate(gen):
    if i >= 15:
        break
    total_proc = int(row['Lab_Test_Count'] + row['Medication_Count'])
    print(f"{row['Patient_ID']:<15} {row['Treatment_Cost']:>15,.2f} {total_proc:>10}")


#ЗАДАЧА 4
print("ЗАДАЧА 4 — Dict и подсчёты")

long_stay = df[df['Days_in_Hospital'] > 10]
dept_long_stay_dict = {}
for dept, group in long_stay.groupby('Department'):
    dept_long_stay_dict[dept] = len(group)

print("\nПациентов с Days_in_Hospital > 10 по отделениям:")
for dept, count in sorted(dept_long_stay_dict.items(), key=lambda x: -x[1]):
    print(f"  {dept}: {count}")

top_dept = max(dept_long_stay_dict, key=dept_long_stay_dict.get)
print(f"\nОтделение с наибольшим кол-вом таких пациентов: {top_dept} ({dept_long_stay_dict[top_dept]})")


#ЗАДАЧА 5
print("ЗАДАЧА 5 — Set и уникальные комбинации")

dept_treatment_combos = set(zip(df['Department'], df['Treatment_Type']))
print(f"\nКоличество уникальных комбинаций (Department, Treatment_Type): {len(dept_treatment_combos)}")
print("\nПримеры 5 комбинаций:")
for combo in list(dept_treatment_combos)[:5]:
    print(f"  {combo}")

#ЗАДАЧА 6
print("ЗАДАЧА 6 — Lambda функции и новые признаки")

df['Treatment_Efficiency'] = df.apply(
    lambda row: row['Treatment_Cost'] / (row['Days_in_Hospital'] + 1), axis=1
)

top10_efficiency = df.nlargest(10, 'Treatment_Efficiency')[
    ['Patient_ID', 'Treatment_Cost', 'Days_in_Hospital', 'Treatment_Efficiency']
]
print("\nТоп-10 пациентов с наибольшей Treatment_Efficiency:")
print(top10_efficiency.to_string(index=False))


#ЗАДАЧА 7
print("ЗАДАЧА 7 — NumPy векторы")

num_data = df[['Age', 'Treatment_Cost', 'Days_in_Hospital', 'Lab_Test_Count']].to_numpy()
print(f"\nФорма массива num_data: {num_data.shape}")
print("Первые 5 строк num_data:")
print(num_data[:5])

eff_array = df['Treatment_Efficiency'].to_numpy()
print(f"\nTreatment_Efficiency — Среднее: {round(np.mean(eff_array), 2)}")
print(f"Treatment_Efficiency — Медиана: {round(np.median(eff_array), 2)}")
print(f"Treatment_Efficiency — Стд. откл.: {round(np.std(eff_array), 2)}")

max_eff_idx = np.argmax(eff_array)
print(f"\nИндекс пациента с макс. Treatment_Efficiency: {max_eff_idx}")
print(f"Patient_ID: {df.iloc[max_eff_idx]['Patient_ID']}, "
      f"Treatment_Efficiency: {round(df.iloc[max_eff_idx]['Treatment_Efficiency'], 2)}")

#ЗАДАЧА 8
print("ЗАДАЧА 8 — Сводные таблицы")

pivot = df.pivot_table(
    index='Department',
    columns='Treatment_Type',
    values='Treatment_Efficiency',
    aggfunc='mean'
)
print("\nСводная таблица — средняя Treatment_Efficiency по (Department, Treatment_Type):")
print(pivot.round(2).to_string())

pivot.to_csv(OUTPUT + 'student3_treatment_efficiency.csv')


#ЗАДАЧА 9
print("ЗАДАЧА 9 — Визуализация Matplotlib")

# Гистограмма Treatment_Cost
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(df['Treatment_Cost'], bins=20, color='steelblue', edgecolor='white', alpha=0.85)
ax.set_title('Распределение стоимости лечения (Treatment_Cost)', fontsize=14, fontweight='bold')
ax.set_xlabel('Стоимость лечения ($)', fontsize=12)
ax.set_ylabel('Количество пациентов', fontsize=12)
ax.grid(axis='y', alpha=0.4)
plt.tight_layout()
plt.savefig(OUTPUT + 'student3_hist_treatment_cost.png', dpi=150)
plt.close()

# Scatter plot: Days_in_Hospital vs Treatment_Cost, цвет по Department
departments = df['Department'].unique()
colors = plt.cm.tab10(np.linspace(0, 1, len(departments)))
dept_color_map = dict(zip(departments, colors))

fig, ax = plt.subplots(figsize=(12, 7))
for dept in departments:
    subset = df[df['Department'] == dept]
    ax.scatter(subset['Days_in_Hospital'], subset['Treatment_Cost'],
               label=dept, color=dept_color_map[dept], alpha=0.5, s=15)

ax.set_title('Зависимость стоимости лечения от дней госпитализации', fontsize=14, fontweight='bold')
ax.set_xlabel('Дни в больнице (Days_in_Hospital)', fontsize=12)
ax.set_ylabel('Стоимость лечения (Treatment_Cost, $)', fontsize=12)
ax.legend(title='Отделение', bbox_to_anchor=(1.01, 1), loc='upper left', fontsize=8)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(OUTPUT + 'student3_scatter_days_cost.png', dpi=150)
plt.close()

#ЗАДАЧА 10
print("ЗАДАЧА 10 — Визуализация Seaborn")
# Countplot по Treatment_Type
fig, ax = plt.subplots(figsize=(10, 6))
order = df['Treatment_Type'].value_counts().index
sns.countplot(data=df, x='Treatment_Type', order=order, palette='Blues_d', ax=ax)
ax.set_title('Количество пациентов по типу лечения', fontsize=14, fontweight='bold')
ax.set_xlabel('Тип лечения', fontsize=12)
ax.set_ylabel('Количество', fontsize=12)
ax.tick_params(axis='x', rotation=25)
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig(OUTPUT + 'student3_countplot_treatment_type.png', dpi=150)
plt.close()


# Boxplot Treatment_Efficiency по Department
fig, ax = plt.subplots(figsize=(12, 6))
dept_order = df.groupby('Department')['Treatment_Efficiency'].median().sort_values(ascending=False).index
sns.boxplot(data=df, x='Department', y='Treatment_Efficiency',
            order=dept_order, palette='Set2', ax=ax)
ax.set_title('Распределение Treatment_Efficiency по отделениям', fontsize=14, fontweight='bold')
ax.set_xlabel('Отделение', fontsize=12)
ax.set_ylabel('Treatment_Efficiency', fontsize=12)
ax.tick_params(axis='x', rotation=20)
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig(OUTPUT + 'student3_boxplot_efficiency_dept.png', dpi=150)
plt.close()

# Heatmap корреляций
corr_cols = ['Age', 'Treatment_Cost', 'Days_in_Hospital',
             'Lab_Test_Count', 'Medication_Count', 'Physical_Therapy_Sessions']
corr_matrix = df[corr_cols].corr()
fig, ax = plt.subplots(figsize=(9, 7))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm',
            center=0, linewidths=0.5, ax=ax)
ax.set_title('Тепловая карта корреляций числовых показателей', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig(OUTPUT + 'student3_heatmap_correlation.png', dpi=150)
plt.close()
