import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#1
df = pd.read_excel("catalog_products.xlsx")
print("="*50)
print(f"Форма DataFrame:{df.shape}")
print(f"Строк:{df.shape[0]}") #строки
print(f"Cтолбцов:{df.shape[1]}") #столбцы
print("\nТипы данных:")
print(df.dtypes.to_string())
missing = df.isnull().sum()
missing_only = missing[missing > 0]
print("\nПропуски (только колонки с пропусками):")
if missing_only.empty:
    print("Пропущенных значений нет.")
else:
    print(missing_only.to_string())
    print(f"\nВсего пропусков: {missing_only.sum()}")
    print(f"Колонок с пропусками: {len(missing_only)}")
print("\nПервые 5 строк:")
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)
print(df.head())

#2
for col in df.columns:
    try:
        df[col] = df[col].astype(float)
    except:
        pass
num_cols = df.select_dtypes(include='number').columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
print("Пропуски в числовых колонках после заполнения:")
print(df[num_cols].isnull().sum())
print("\nТипы числовых колонок после преобразования:")
print(df[num_cols].dtypes)

#3
df['total_value'] = df['col_2'] * df['col_3']
df['double_stock'] = df['col_4'] * 2
df['log_price'] = np.log(df['col_2'].replace(0, np.nan))  #логарифм нуля не определен
print(df[['col_2', 'col_3', 'col_4', 'total_value', 'double_stock', 'log_price']].head())

#4
electronics_expensive = df[(df['col_2'] > 500) & (df['col_7'] == 'Electronics')]
print(electronics_expensive.head())

#5
result = df.groupby('col_7').agg(
    mean_price=('col_2', 'mean'),
    max_price=('col_2', 'max'),
    total_quantity=('col_3', 'sum')
).reset_index().rename(columns={'col_7': 'category'})
print(result)

#6
num_only_cols = df.select_dtypes(include='number').columns[:9].tolist()
stats = df[num_only_cols].agg(['mean', 'median', 'std']).T.reset_index()
stats.columns = ['column', 'mean', 'median', 'std']
print(stats)

#7
mean = df['col_2'].mean()
std = df['col_2'].std()
anomalies = df[df['col_2'] > mean + 3 * std]
print(f"Аномальных товаров: {len(anomalies)}")
print(anomalies.head())

#8
num_only_cols = df.select_dtypes(include='number').columns[:9].tolist()
corr_matrix = df[num_only_cols].corr()
print(corr_matrix.round(2))

#9
plt.figure(figsize=(10, 5))
plt.hist(df['col_2'], bins=50, color='steelblue', edgecolor='white')
plt.title('Распределение цены товаров')
plt.xlabel('Цена')
plt.ylabel('Количество товаров')
plt.grid(True)
plt.show()

#10
sns.regplot(data=df, x='col_2', y='col_3', scatter_kws={'alpha': 0.3})
plt.title('Взаимосвязь цены и количества на складе')
plt.xlabel('Цена (col_2)')
plt.ylabel('Количество на складе (col_3)')
plt.tight_layout()
plt.show()

#11
df.boxplot(column='col_2', by='col_7', figsize=(10, 5))
plt.title('Распределение цены по категориям')
plt.suptitle('')
plt.xlabel('Категория')
plt.ylabel('Цена')
plt.grid(True)
plt.show()

#12
cols12 = ['col_2', 'col_3', 'col_4', 'col_5', 'col_6', 'col_7']
sns.pairplot(df[cols12], hue='col_7')
plt.suptitle('Парные диаграммы по категориям', y=1.02)
plt.show()

#13
num_only_cols = df.select_dtypes(include='number').columns[:9].tolist()
corr = df[num_only_cols].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Тепловая карта корреляции')
plt.show()

#14
df.to_excel('catalog_analysis.xlsx', index=False)
print("Файл сохранён: catalog_analysis.xlsx")

#15
category_summary = df.groupby('col_7').agg(
    count=('col_2', 'count'),
    mean_price=('col_2', 'mean'),
    total_quantity=('col_3', 'sum'),
    mean_log_price=('log_price', 'mean')
).reset_index()
category_summary.columns = ['category', 'count', 'mean_price', 'total_quantity', 'mean_log_price']
print(category_summary.head())

#16
most_expensive = df.loc[df.groupby('col_7')['col_2'].idxmax(), ['col_1', 'col_2', 'col_7']]
print(most_expensive)

#17
category_summary = df.groupby('col_7').agg(
    count=('col_2', 'count'),
    mean_price=('col_2', 'mean'),
    total_quantity=('col_3', 'sum'),
    mean_log_price=('log_price', 'mean')
).reset_index()
category_summary.columns = ['category', 'count', 'mean_price', 'total_quantity', 'mean_log_price']
print(category_summary.head())

#18
bins = [0, 50, 200, 500, 1000, float('inf')]
labels = ['0-50', '50-200', '200-500', '500-1000', '>1000']
df['price_range'] = pd.cut(df['col_2'], bins=bins, labels=labels)
price_counts = df['price_range'].value_counts().sort_index().reset_index()
price_counts.columns = ['price_range', 'count']
sns.barplot(data=price_counts, x='price_range', y='count')
plt.title('Распределение товаров по диапазонам цен')
plt.xlabel('Диапазон цен')
plt.ylabel('Количество товаров')
plt.show()
print(price_counts)

#19
category_value = df.groupby('col_7', group_keys=False).apply(
    lambda x: (x['col_2'] * x['col_3']).sum()
).reset_index()
category_value.columns = ['category', 'total_stock_value']
top_category = category_value.loc[category_value['total_stock_value'].idxmax(), 'category']
print(f"Категория с наибольшей стоимостью: {top_category}")
plt.figure(figsize=(10, 5))
plt.bar(category_value['category'], category_value['total_stock_value'], color='steelblue')
plt.title('Суммарная стоимость товаров по категориям')
plt.xlabel('Категория')
plt.ylabel('Суммарная стоимость')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

#20
category_stats = df.groupby('col_7').agg(
    mean_price=('col_2', 'mean'),
    mean_quantity=('col_3', 'mean')
).reset_index()
sns.scatterplot(data=category_stats, x='mean_price', y='mean_quantity', hue='col_7', s=100)
plt.title('Средняя цена vs Средний запас по категориям')
plt.xlabel('Средняя цена')
plt.ylabel('Средний запас')
plt.show()
print(category_stats)

#21
std_by_category = df.groupby('col_7')['col_2'].std().reset_index()
std_by_category.columns = ['category', 'std_price']
std_by_category = std_by_category.sort_values('std_price', ascending=True)
plt.figure(figsize=(10, 5))
plt.barh(std_by_category['category'], std_by_category['std_price'], color='steelblue')
plt.title('Разброс цены по категориям')
plt.xlabel('Стандартное отклонение цены')
plt.ylabel('Категория')
plt.grid(True)
plt.tight_layout()
plt.show()

#22
out_of_stock = df[df['col_3'] == 0][['col_1', 'col_7', 'col_2']]
print(f"Товаров с нулевым запасом: {len(out_of_stock)}")
print(out_of_stock.head(10))

#23
top5 = df.groupby('col_7')['col_1'].count().nlargest(5).reset_index()
top5.columns = ['category', 'count']
print(top5)
plt.figure(figsize=(8, 5))
plt.bar(top5['category'], top5['count'], color='steelblue')
plt.title('Топ-5 категорий по количеству товаров')
plt.xlabel('Категория')
plt.ylabel('Количество товаров')
plt.grid(True)
plt.tight_layout()
plt.show()

#24
top10 = df.nlargest(10, 'col_3')[['col_1', 'col_3']]
sns.barplot(data=top10, x='col_3', y='col_1')
plt.title('Топ-10 товаров по количеству на складе')
plt.xlabel('Количество на складе')
plt.ylabel('Товар')
plt.tight_layout()
plt.show()
print(top10)

#25
bins = [0, 50, 200, 500, 1000, float('inf')]
labels = ['0-50', '50-200', '200-500', '500-1000', '>1000']
df['price_range'] = pd.cut(df['col_2'], bins=bins, labels=labels)
pivot = df.pivot_table(index='col_7', columns='price_range', values='col_1', aggfunc='count', fill_value=0)
sns.heatmap(pivot, annot=True, fmt='d', cmap='YlOrRd')
plt.show()

#36
category_stats = df.groupby('col_7').agg(
    mean_price=('col_2', 'mean'),
    mean_quantity=('col_3', 'mean')
).reset_index()
sns.scatterplot(data=category_stats, x='mean_price', y='mean_quantity', hue='col_7', s=100)
plt.title('Сравнение категорий по средней цене и запасу')
plt.xlabel('Средняя цена')
plt.ylabel('Средний запас')
plt.show()
print(category_stats)

#37
std_by_cat = df.groupby('col_7')['col_2'].std().sort_values().reset_index()
plt.barh(std_by_cat['col_7'], std_by_cat['col_2'])
plt.show()

#38
out_of_stock = df[df['col_3'] == 0][['col_1', 'col_7', 'col_2']]
print(f"Товаров без запаса: {len(out_of_stock)}")
print(out_of_stock.head(10))

#39
top5 = df.groupby('col_7')['col_1'].count().nlargest(5)
top5.plot(kind='bar')
plt.show()

#40
top10 = df.nlargest(10, 'col_3')[['col_1', 'col_3']]
sns.barplot(data=top10, x='col_3', y='col_1')
plt.title('Топ-10 товаров по количеству на складе')
plt.xlabel('Количество на складе')
plt.ylabel('Товар')
plt.tight_layout()
plt.show()
print(top10)

#42
sns.regplot(data=df, x='col_2', y='col_5', scatter_kws={'alpha': 0.3})
plt.title('Взаимосвязь цены и рейтинга товаров')
plt.xlabel('Цена (col_2)')
plt.ylabel('Рейтинг (col_5)')
plt.tight_layout()
plt.show()

#43
sns.pairplot(df[['col_2', 'col_3', 'col_4', 'col_5', 'col_6', 'col_7']], hue='col_7')
plt.show()

#44
mean_price, std_price = df['col_2'].mean(), df['col_2'].std()
mean_stock, std_stock = df['col_3'].mean(), df['col_3'].std()
extreme_items = df[
    (df['col_2'] > mean_price + 3 * std_price) |
    (df['col_3'] > mean_stock + 3 * std_stock)
]
print(f"Аномальных товаров: {len(extreme_items)}")
print(extreme_items[['col_1', 'col_2', 'col_3', 'col_7']].head())

#45
with pd.ExcelWriter('catalog_final_report.xlsx') as writer:
    df.to_excel(writer, sheet_name='Данные', index=False)
    df.groupby('col_7').agg(mean_price=('col_2', 'mean'), total_quantity=('col_3', 'sum')).to_excel(writer, sheet_name='Категории')
    df.nlargest(10, 'total_value')[['col_1', 'col_2', 'col_3', 'total_value']].to_excel(writer, sheet_name='Топ10', index=False)
