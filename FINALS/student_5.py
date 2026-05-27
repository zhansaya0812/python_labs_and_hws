import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


#1
print("Задача 1 — Проверка и очистка")
df = pd.read_excel("hospital_patient_treatment.xlsx")
print("\nТипы данных всех колонок:")
print(df.dtypes)

print("\nКолонки с пропущенными значениями:")
missing = df.isnull().sum()
missing_cols = missing[missing > 0]

if missing_cols.empty:
    print("Пропущенных значений не обнаружено.")
else:
    print(missing_cols)
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in missing_cols.index:
        if col in numeric_cols:
            df[col] = df[col].fillna(df[col].mean())
            print(f"  → Колонка '{col}' заполнена средним значением.")


df["activity_score"] = (
    df["Lab_Test_Count"] +
    df["Medication_Count"] +
    df["Physical_Therapy_Sessions"]
)

print("\nСтатистика по Treatment_Cost:")
print(df["Treatment_Cost"].describe().round(2))

print("\nСтатистика по Days_in_Hospital:")
print(df["Days_in_Hospital"].describe().round(2))

print("\nСтатистика по activity_score:")
print(df["activity_score"].describe().round(2))


#2
print("Задача 2 — Фильтрация по комплексным условиям")
total_procedures = (
    df["Lab_Test_Count"] +
    df["Physical_Therapy_Sessions"] +
    df["Medication_Count"]
)

filtered_df = df[
    (total_procedures >= 15) &
    (df["Treatment_Cost"] >= 5000) &
    (df["Days_in_Hospital"] >= 7)
].copy()

filtered_df["total_procedures"] = (
    filtered_df["Lab_Test_Count"] +
    filtered_df["Physical_Therapy_Sessions"] +
    filtered_df["Medication_Count"]
)

avg_cost = filtered_df["Treatment_Cost"].mean()
print(f"\nКоличество отфильтрованных пациентов: {len(filtered_df)}")
print(f"Средний Treatment_Cost среди них: {avg_cost:.2f}")

print("\nПервые 10 пациентов (Patient_ID, сумма процедур, Treatment_Cost):")
print(filtered_df[["Patient_ID", "total_procedures", "Treatment_Cost"]].head(10).to_string(index=False))


#3
print("Задача 3 — Повторный анализ")
def high_activity_patients(df, min_total_sessions, min_cost):

    total = (
        df["Lab_Test_Count"] +
        df["Medication_Count"] +
        df["Physical_Therapy_Sessions"]
    )
    result = df[(total >= min_total_sessions) & (df["Treatment_Cost"] >= min_cost)].copy()
    result["total_procedures"] = total[result.index]
    return result

result_df = high_activity_patients(df, min_total_sessions=12, min_cost=4000)

print(f"\nНайдено пациентов с >= 12 процедур и Treatment_Cost >= 4000: {len(result_df)}")
print("\nПервые 10 строк результата:")
print(result_df[["Patient_ID", "total_procedures", "Treatment_Cost", "Department"]].head(10).to_string(index=False))


#4
print("Задача 4 — Comprehension и условные конструкции")
mask = (
    (df["Lab_Test_Count"] + df["Medication_Count"] + df["Physical_Therapy_Sessions"] >= 10) &
    (df["Days_in_Hospital"] <= 5)
)
short_stay_active = df.loc[mask, "Patient_ID"].tolist()

print(f"\nКоличество пациентов в списке short_stay_active: {len(short_stay_active)}")
print("Первые 10 элементов:")
print(short_stay_active[:10])


#5
print("Задача 5 — Lambda и новые показатели")
df["treatment_efficiency"] = df.apply(
    lambda row: (
        row["Lab_Test_Count"] + row["Medication_Count"] + row["Physical_Therapy_Sessions"]
    ) / (row["Treatment_Cost"] + 1) * 100,
    axis=1
)

top10_efficiency = df.nlargest(10, "treatment_efficiency")[
    ["Patient_ID", "Lab_Test_Count", "Medication_Count",
     "Physical_Therapy_Sessions", "Treatment_Cost", "treatment_efficiency"]
]

print("\nТоп-10 пациентов с наибольшей treatment_efficiency:")
print(top10_efficiency.to_string(index=False))


#6
print("Задача 6 — Циклы и категории пациентов")
categories = []
for val in df["treatment_efficiency"]:
    if val >= 2:
        categories.append("Premium")
    elif val >= 1:
        categories.append("Standard")
    else:
        categories.append("Low")

df["patient_category"] = categories

print("\nРаспределение по категориям:")
print(df["patient_category"].value_counts())

print("\nРаспределение категорий по отделениям (Department):")
dept_cat = df.groupby(["Department", "patient_category"]).size().unstack(fill_value=0)
print(dept_cat)


#7
print("Задача 7 — OOP и классы")
class HospitalPatient:
    def __init__(self, patient_id, lab_test_count, medication_count,
                 physical_therapy_sessions, treatment_cost):
        self.patient_id = patient_id
        self.lab_test_count = lab_test_count
        self.medication_count = medication_count
        self.physical_therapy_sessions = physical_therapy_sessions
        self.treatment_cost = treatment_cost

    def efficiency(self):
        total_sessions = (
            self.lab_test_count +
            self.medication_count +
            self.physical_therapy_sessions
        )
        return total_sessions / (self.treatment_cost + 1) * 100

    def __repr__(self):
        return (f"HospitalPatient({self.patient_id}, "
                f"efficiency={self.efficiency():.4f})")


patient_objects = [
    HospitalPatient(
        patient_id=row["Patient_ID"],
        lab_test_count=row["Lab_Test_Count"],
        medication_count=row["Medication_Count"],
        physical_therapy_sessions=row["Physical_Therapy_Sessions"],
        treatment_cost=row["Treatment_Cost"]
    )
    for _, row in df.head(20).iterrows()
]

print("\nПоказатель efficiency() для первых 20 пациентов:")
for patient in patient_objects:
    print(f"  {patient.patient_id}: {patient.efficiency():.4f}")


#8
print("Задача 8 — Функции и сводные таблицы")
def pivot_analysis(df, index_col, value_col):

    pivot = df.pivot_table(
        index=index_col,
        columns="Treatment_Type",
        values=value_col,
        aggfunc="mean"
    ).round(4)
    return pivot

pivot_result = pivot_analysis(df, "Department", "treatment_efficiency")

print("\nСредняя treatment_efficiency по Department и Treatment_Type:")
print(pivot_result.to_string())

pivot_result.to_csv("student5_treatment_efficiency.csv")


#9
print("Задача 9 — Matplotlib")
color_map = {"Premium": "#2ecc71", "Standard": "#3498db", "Low": "#e74c3c"}

df["total_procedures"] = (
    df["Lab_Test_Count"] + df["Medication_Count"] + df["Physical_Therapy_Sessions"]
)

fig, ax = plt.subplots(figsize=(10, 6))

for category, color in color_map.items():
    subset = df[df["patient_category"] == category]
    ax.scatter(
        subset["Treatment_Cost"],
        subset["total_procedures"],
        c=color,
        label=category,
        alpha=0.5,
        s=18,
        edgecolors="none"
    )

ax.set_xlabel("Стоимость лечения (Treatment_Cost)", fontsize=12)
ax.set_ylabel("Сумма процедур (Lab + Medication + Therapy)", fontsize=12)
ax.set_title("Зависимость суммы процедур от стоимости лечения\nпо категориям пациентов", fontsize=13)
ax.legend(title="Категория пациента", fontsize=10)
ax.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("student5_scatter_cost_vs_procedures.png", dpi=150)
plt.close()


#10
print("Задача 10 — Seaborn")
sns.set_theme(style="whitegrid", palette="muted")

#Countplot: patient_category по Department ---
fig, ax = plt.subplots(figsize=(12, 6))
sns.countplot(
    data=df,
    x="Department",
    hue="patient_category",
    palette={"Premium": "#2ecc71", "Standard": "#3498db", "Low": "#e74c3c"},
    ax=ax
)
ax.set_title("Распределение категорий пациентов по отделениям", fontsize=13)
ax.set_xlabel("Отделение", fontsize=11)
ax.set_ylabel("Количество пациентов", fontsize=11)
ax.tick_params(axis="x", rotation=30)
ax.legend(title="Категория пациента")
plt.tight_layout()
plt.savefig("student5_countplot_categories_by_dept.png", dpi=150)
plt.close()


#Boxplot: treatment_efficiency по Treatment_Type
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(
    data=df,
    x="Treatment_Type",
    y="treatment_efficiency",
    palette="Set2",
    ax=ax
)
ax.set_title("Распределение эффективности лечения по типу лечения", fontsize=13)
ax.set_xlabel("Тип лечения", fontsize=11)
ax.set_ylabel("treatment_efficiency", fontsize=11)
plt.tight_layout()
plt.savefig("student5_boxplot_efficiency_by_type.png", dpi=150)
plt.close()


all_numeric_features = [
    "Lab_Test_Count", "Medication_Count", "Physical_Therapy_Sessions",
    "Treatment_Cost", "Days_in_Hospital", "treatment_efficiency",
    "Heart_Rate", "BMI", "Age", "Risk_Score"
]
numeric_features = [col for col in all_numeric_features if col in df.columns]

corr_matrix = df[numeric_features].corr().round(2)

fig, ax = plt.subplots(figsize=(11, 8))
sns.heatmap(
    corr_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0,
    linewidths=0.5,
    ax=ax
)
ax.set_title("Матрица корреляций числовых показателей активности и затрат", fontsize=13)
plt.tight_layout()
plt.savefig("student5_heatmap_correlations.png", dpi=150)
plt.close()
