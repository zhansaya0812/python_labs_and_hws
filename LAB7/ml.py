import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#1
df=pd.read_excel("catalog_products.xlsx")
pd.set_option("display.max_columns",None)
pd.set_option("display.width",200)
print("="*50)
print(f"Форма DataFrame:{df.shape}")
print(f"Строк:{df.shape[0]}")
print(f"Столбцов:{df.shape[1]}")
print("\nТипы данных:")
print(df.dtypes.to_string())
missing=df.isnull().sum()
missing_only=missing[missing>0]
print("\nПропуски:")
if missing_only.empty:
    print("Пропущенных значений нет.")
else:
    print(missing_only.to_string())
    print(f"Всего пропусков:{missing_only.sum()}")
print("\nПервые 5 строк:")
print(df.head())
#2
for col in df.columns:
    try:
        df[col]=df[col].astype(float)
    except:
        pass
num_cols=df.select_dtypes(include='number').columns
df[num_cols]=df[num_cols].fillna(df[num_cols].mean())
df.dropna(subset=['col_1','col_7'],inplace=True)
print("\nПропуски после очистки:")
print(df.isnull().sum()[df.isnull().sum()>0])
#3
df['total_value']=df['col_2']*df['col_3']
df['log_price']=np.log(df['col_2'].replace(0,np.nan))
df['double_stock']=df['col_3']*2
print("Новые признаки (первые 5 строк):")
print(df[['col_2','col_3','total_value','log_price','double_stock']].head())
#4
#1)
plt.figure(figsize=(10,5))
plt.hist(df['col_2'],bins=50,color='steelblue',edgecolor='white')
plt.title('Распределение цены товаров')
plt.xlabel('Цена')
plt.ylabel('Количество товаров')
plt.grid(True)
plt.tight_layout()
plt.show()
#2)
sns.regplot(data=df,x='col_2',y='col_3',scatter_kws={'alpha':0.3})
plt.title('Цена vs Количество на складе')
plt.xlabel('Цена (col_2)')
plt.ylabel('Количество (col_3)')
plt.tight_layout()
plt.show()
#3)
df.boxplot(column='col_2',by='col_7',figsize=(10,5))
plt.title('Распределение цены по категориям')
plt.suptitle('')
plt.xlabel('Категория')
plt.ylabel('Цена')
plt.grid(True)
plt.tight_layout()
plt.show
#5
mean=df['col_2'].mean()
std=df['col_2'].std()
anomalies=df[(df['col_2']>mean+3*std)|(df['col_2']<mean-3*std)]
print(f"\nАномальных товаров:{len(anomalies)}")
print(anomalies[['col_1','col_2','col_7']].head())
df_clean=df[~((df['col_2']>mean+3*std)|(df['col_2']<mean-3*std))].copy()
print(f"Строк после удаления аномалий:{len(df_clean)}")