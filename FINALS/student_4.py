import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import filedialog
import sys

# Автоматты түрде файл таңдау терезесін ашу
print("Қазір экранда файл таңдау терезесі ашылады...")
root = tk.Tk()
root.withdraw()  # Негізгі терезені жасыру

# Файлды таңдау терезесі
file_path = filedialog.askopenfilename(
    title="Өзіңіздің Excel немесе CSV файлыңызды таңдаңыз",
    filetypes=[("Excel Files", "*.xlsx *.xls"), ("CSV Files", "*.csv")]
)

if not file_path:
    print("ҚАТЕ: Файл таңдалмады! Кодты қайта қосып, файлды таңдаңыз.")
    sys.exit()

print(f"Жүктелген файл: {file_path}\n")

# Файл форматына қарай (Excel не CSV) автоматты түрде оқу
if file_path.endswith('.csv'):
    df = pd.read_csv(file_path)
else:
    df = pd.read_excel(file_path)


#Задача 1 — Загрузка данных и первичный анализ
print("Задача 1 — Загрузка данных и первичный анализ")
print("Первые 10 строк данных")
print(df.head(10))

active_condition_1 = (df['Lab_Test_Count'] + df['Physical_Therapy_Sessions']) >= 10
active_patients_count = df[active_condition_1].shape[0]
print(f"Количество активных пациентов: {active_patients_count}")

mean_cost_1 = df[active_condition_1]['Treatment_Cost'].mean()
mean_days_1 = df[active_condition_1]['Days_in_Hospital'].mean()
print(f"Средняя стоимость лечения: {mean_cost_1:.2f}")
print(f"Среднее количество дней в больнице: {mean_days_1:.1f}\n")


#Задача 2 — Фильтрация и работа со строками
print("Задача 2 — Фильтрация и работа со строками")
sum_activity = df['Lab_Test_Count'] + df['Medication_Count'] + df['Physical_Therapy_Sessions']
filtered_df_2 = df[sum_activity >= 15]
patient_ids_upper = filtered_df_2['Patient_ID'].astype(str).str.upper().tolist()
print(f"Количество пациентов с активностью >= 15: {len(patient_ids_upper)}")
print("Первые 5 Patient_ID в верхнем регистре:", patient_ids_upper[:5])
mean_cost_2 = filtered_df_2['Treatment_Cost'].mean()
print(f"Средний Treatment_Cost активных пациентов: {mean_cost_2:.2f}\n")


#Задача 3 — Generator
print("#Задача 3 — Generator")
physio_patients = (
    row for row in df.itertuples()
    if row.Treatment_Type == "Therapy" and (row.Physical_Therapy_Sessions + row.Lab_Test_Count) > 8
)
print(f"{'Patient_ID':<15} | {'Department':<15} | {'Physio_Sessions':<15}")
print("-" * 55)
try:
    for _ in range(15):
        p = next(physio_patients)
        print(f"{p.Patient_ID:<15} | {p.Department:<15} | {p.Physical_Therapy_Sessions:<15}")
except StopIteration:
    print("--- Данные в генераторе закончились ---")
print("\n")


#Задача 4 — Comprehension и условные конструкции
print("Задача 4 — Comprehension и условные конструкции")
short_stay_active = [
    row.Patient_ID for row in df.itertuples()
    if (row.Lab_Test_Count + row.Medication_Count + row.Physical_Therapy_Sessions) >= 10
    and row.Days_in_Hospital <= 5
]
print(f"Длина списка short_stay_active: {len(short_stay_active)}")
print("Первые 10 элементов:", short_stay_active[:10])
print("\n")


#(Старая Задача 5, чтобы не терять код)
print("=== СВЯЗКА ДАННЫХ (SET) ===")
active_condition_5 = (df['Lab_Test_Count'] + df['Medication_Count'] + df['Physical_Therapy_Sessions']) >= 10
active_df_5 = df[active_condition_5]
unique_combinations = set(zip(active_df_5['Department'], active_df_5['Treatment_Type']))
print(f"Количество уникальных комбинаций: {len(unique_combinations)}")
print("\n")



#Задача 5 — Lambda и новые показатели
print("Задача 5 — Lambda и новые показатели")
# Добавляем колонку treatment_efficiency
df['treatment_efficiency'] = df.apply(
    lambda row: (row['Lab_Test_Count'] + row['Medication_Count'] + row['Physical_Therapy_Sessions']) / (row['Treatment_Cost'] + 1) * 100,
    axis=1
)

# Выводим топ-10 пациентов
top_10_efficiency = df.sort_values(by='treatment_efficiency', ascending=False).head(10)
print("--- Топ-10 пациентов с наибольшей treatment_efficiency ---")
print(top_10_efficiency[['Patient_ID', 'Department', 'treatment_efficiency']])
print("\n")


#Задача 6 — Lambda
print("Задача 6 — Lambda")
df['activity_score'] = df.apply(
    lambda row: (row['Lab_Test_Count'] + row['Medication_Count'] + row['Physical_Therapy_Sessions']) / (row['Treatment_Cost'] + 1),
    axis=1
)
top_10_activity = df.sort_values(by='activity_score', ascending=False).head(10)
print("--- Топ-10 пациентов по activity_score ---")
print(top_10_activity[['Patient_ID', 'Department', 'activity_score']])
print("\n")


#Задача 7 — NumPy
print("Задача 7 — NumPy")
activity_data = df[['Lab_Test_Count', 'Medication_Count', 'Physical_Therapy_Sessions']].to_numpy()
means = np.mean(activity_data, axis=0)
stds = np.std(activity_data, axis=0)
metrics = ['Lab_Test_Count', 'Medication_Count', 'Physical_Therapy_Sessions']
for i, metric in enumerate(metrics):
    print(f"{metric:<25} | Среднее: {means[i]:.2f} | Стд. откл: {stds[i]:.2f}")
print("-" * 50)
sum_per_patient = np.sum(activity_data, axis=1)
max_activity_idx = np.argmax(sum_per_patient)
print(f"Индекс пациента с максимальной активностью: {max_activity_idx}\n")


#Задача 8 — Сводные таблицы
print("Задача 8 — Сводные таблицы")
pivot_activity = df.pivot_table(index='Department', columns='Treatment_Type', values='activity_score', aggfunc='mean')
pivot_cost = df.pivot_table(index='Department', columns='Treatment_Type', values='Treatment_Cost', aggfunc='mean')
pivot_activity.to_csv('pivot_activity_score.csv')
pivot_cost.to_csv('pivot_treatment_cost.csv')
print("Сводные таблицы сохранены в CSV файлы!\n")


#Задача 9 — Matplotlib
print("Задача 9 — Matplotlib")
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.hist(df['Lab_Test_Count'], bins=20, color='skyblue', edgecolor='black')
plt.title('Распределение Lab_Test_Count')
plt.grid(True, linestyle='--', alpha=0.5)

plt.subplot(1, 2, 2)
departments = df['Department'].unique()
for dept in departments:
    dept_df = df[df['Department'] == dept]
    plt.scatter(dept_df['Treatment_Cost'], dept_df['activity_score'], label=dept, alpha=0.6)
plt.title('Treatment_Cost vs activity_score')
plt.legend(title='Отделения')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('matplotlib_plots.png')
plt.show()


#Задача 10 — Seaborn
print("Задача 10 — Seaborn")
sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 4))
sns.countplot(data=df[df['activity_score'] >= 1], x='Treatment_Type', palette='Set2')
plt.title('Количество пациентов с activity_score >= 1')
plt.show()

plt.figure(figsize=(10, 5))
sns.boxplot(data=df, x='Department', y='activity_score', hue='Department', palette='Pastel1', legend=False)
plt.xticks(rotation=45)
plt.title('Распределение activity_score по отделениям')
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 5))
corr_columns = ['Lab_Test_Count', 'Medication_Count', 'Physical_Therapy_Sessions', 'Treatment_Cost', 'Days_in_Hospital']
sns.heatmap(df[corr_columns].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Матрица корреляции')
plt.tight_layout()
plt.show()