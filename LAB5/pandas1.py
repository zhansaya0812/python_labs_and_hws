from fastapi import FastAPI
import pandas as pd
from datetime import datetime
from datetime import date
import numpy as np

#BLOCK1
#1
class User:
    def __init__(self, _id:int, _name:str,_email:str):
        self._id = _id
        self._name = _name.strip().title()
        _email = _email.lower()
        if "@" not in _email:
            raise ValueError("Invalid email address")
        self._email = _email
    def __str__(self):
        return f"User(id={self._id}, name={self._name}, email={self._email})"
    def __del__(self):
        print(f"User{self._name} deleted")

#2
    @classmethod
    def from_string(cls,data:str):
        parts= data.split(",")
        _id = int(parts[0].strip())
        _name = parts[1].strip()
        _email = parts[2].strip()
        return cls(_id,_name,_email)
#3
class Product:
    def __init__(self, id:int, name:str, price:float, category:str):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
    def __str__(self):
        return f"Product(id={self.id}, name={self.name}, price={self.price}, category={self.category})"
    def __eq__(self,other):
        if isinstance(other,Product):
            return self.id == other.id
        return False
    def __hash__(self):
        return hash(self.id)
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "category": self.category,
        }
#4
class Inventory:
    def __init__(self):
        self._products ={}
    def add_product(self, product:Product):
        if product.id in self._products:
            print(f"Product {product.id} already exists")
            return
        self._products[product.id] = product
    def remove_product(self, product_id:int):
        if product_id not in self._products:
            raise ValueError(f"Product {product_id} does not exist")
        del self._products[product_id]
    def get_product(self, product_id:int):
        if product_id not in self._products:
            raise ValueError(f"Product {product_id} does not exist")
        return self._products[product_id]
    def get_all_products(self):
        return list(self._products.values())
    def unique_products(self):
        return set(self._products.values())
    def to_dict(self):
        return dict(self._products)
#5
    def filter_by_price(self,min_price:float):
        is_expensive= lambda p: p.price>=min_price
        return [p for p in self._products.values() if is_expensive(p)]
#6
class Logger:
    def log_action(self,user: User, action: str, product: Product, filename: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line= f"{timestamp};{user._id};{action};{product.id}\n"
        with open(filename,"a") as f:
            f.write(line)
    def read_logs(self, filename: str):
        logs=[]
        with open(filename,"r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(";")
                logs.append({
                    "timestamp": parts[0],
                    "user._id": parts[1],
                    "action": parts[2],
                    "product_id": parts[3]
                })
        return logs
#7
class Order:
    def __init__(self, id:int, user:User):
        self.id = id
        self.user = user
        self.products: list = []
    def add_product(self, product:Product):
        self.products.append(product)
    def remove_product(self, product_id:int):
        for p in self.products:
            if p.id == product_id:
                self.products.remove(p)
                return
        raise ValueError(f"Product {product_id} not found in order")
    def total_price(self):
        return sum(p.price for p in self.products)
    def __str__(self):
        product_names = ", ".join(p.name for p in self.products)
        return (f"Order(id={self.id},user='{self.user._name}',"
                f"products=[{product_names}],total={self.total_price()})")
#8
    def most_expensive_products(self,n:int):
        return sorted(self.products, key=lambda p: p.price, reverse=True)[:n]
#9
def price_stream(products:list):
    for product in products:
        yield product.price
#10
class OrderIterator:
    def __init__(self, orders:list):
        self._orders = orders
        self._index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self._index>= len(self._orders):
            raise StopIteration
        order = self._orders[self._index]
        self._index += 1
        return order
#BLOCK2
#11
def get_price_array(products):
    return np.array([p.price for p in products],dtype=float)

#12
def mean_median_price(prices:np.ndarray):
    mean_price = round(float(np.mean(prices)),2)
    median_price = round(float(np.median(prices)),2)
    return (mean_price, median_price)
#13
def normalize_prices(prices:np.ndarray):
    min_price = np.min(prices)
    max_price = np.max(prices)
    return np.round((prices-min_price)/(max_price-min_price),4)
#14
def category_of_products(products:list):
    return np.array([p.category for p in products])
#15
def count_unique_categories(categories:np.ndarray):
    return len(np.unique(categories))
#16
def products_above_mean(prices:np.ndarray,products:list):
    mean_price = np.mean(prices)
    return[p for p,price in zip(products,prices) if price>mean_price]
#17
def sales_price(prices:np.ndarray,discount:float=0.10):
    return np.round(prices*(1-discount),2)
#18
def orders_2d(orders):
    totals=[]
    for order in orders:
        total_price=sum(p.price for p in order.products)
        totals.append(total_price)
    return np.array(totals)
#19
def average_order_per_user(orders_array:np.ndarray):
    return round(float(np.mean(orders_array)),2)
#20
def expensive_order_indices(orders_array:np.ndarray):
    return np.where(orders_array>1000)[0]
#BLOCK3
#21
def users_to_dataframe(users):
    return pd.DataFrame({
        "id": [u._id for u in users],
        "name": [u._name for u in users],
        "email": [u._email for u in users],
        "registration_date": date.today()
    })
#22
def products_to_dataframe(products:list):
    return pd.DataFrame({
        "id":[p.id for p in products],
        "name":[p.name for p in products],
        "category":[p.category for p in products],
        "price":[p.price for p in products]
    })
#23
def orders_to_dataframe(orders:list):
    return pd.DataFrame({
        "order_id":[o.id for o in orders],
        "user_id":[o.user._id for o in orders],
        "total": [o.total_price() for o in orders]
    })
def merge_users_orders(users_df:pd.DataFrame,orders_df:pd.DataFrame):
    merged=pd.merge(orders_df,users_df[["id","name"]],left_on="user_id",right_on="id")
    return merged[["order_id","name","total"]].rename(columns={"name":"user_name"})
#24
def filter_orders_by_total(merged_df:pd.DataFrame,min_total:float):
    return merged_df[merged_df["total"]>min_total]
#25
def group_orders_by_user(merged_df:pd.DataFrame):
    return (merged_df.groupby("user_name")["total"]
            .sum()
            .reset_index()
            .rename(columns={"total":"total_sum"}))
#26
def mean_order_by_user(merged_df:pd.DataFrame):
    return (merged_df.groupby("user_name")["total"]
            .mean()
            .reset_index()
            .rename(columns={"total":"total_mean"}))
#27
def count_orders_by_user(merged_df:pd.DataFrame):
    return (merged_df.groupby("user_name")["order_id"]
            .count()
            .reset_index()
            .rename(columns={"order_id":"orders_count"}))
#28
def mean_price_by_category(products_df:pd.DataFrame):
    return (products_df.groupby("category")["price"]
            .mean()
            .reset_index()
            .rename(columns={"price":"mean_price"})

    )
#29
def add_sale_price(products_df:pd.DataFrame,discount:float=0.10):
    products_df=products_df.copy()
    products_df["sale_price"]=products_df["price"]*(1-discount)
    return products_df
#30
def sort_products_by_price(products_df:pd.DataFrame):
    return products_df.sort_values("price",ascending=False).reset_index(drop=True)
#31
def add_quantity(orders_products_df:pd.DataFrame):
    orders_products_df=orders_products_df.copy()
    orders_products_df["quantity"]=1
    return orders_products_df
#32
def add_total_price(orders_products_df:pd.DataFrame):
    orders_products_df=orders_products_df.copy()
    orders_products_df["total_price"]=orders_products_df["total"]*orders_products_df["quantity"]
    return orders_products_df
#33
def filter_by_category(products_df:pd.DataFrame,category:str):
    return products_df[products_df["category"]==category].reset_index(drop=True)
#34
def count_products_by_category(products_df:pd.DataFrame):
    return (products_df.groupby("category")["name"]
            .count()
            .reset_index()
            .rename(columns={"name":"count"}))
#35
def average_price_by_category(products_df:pd.DataFrame):
    return (products_df.groupby("category")["price"]
            .mean()
            .reset_index()
            .rename(columns={"price":"mean_price"}))
#36
def sort_orders_by_total(products_df:pd.DataFrame):
    return products_df.sort_values("total_price",ascending=False).reset_index(drop=True)
#37
def top_n_orders(products_df:pd.DataFrame,n:int=3):
    return products_df.sort_values("total_price",ascending=False).head(n).reset_index(drop=True)
#38 same as 23
#39 same as 26
#40 same as 27
#41
def max_orders_by_user(merged_df:pd.DataFrame):
    return (merged_df.groupby("user_name")["total"]
            .max()
            .reset_index()
            .rename(columns={"total":"max_order"}))
#42
def orders_products_with_user(orders:list):
    rows=[]
    for o in orders:
        for p in o.products:
            rows.append({
                "user_name":o.user._name,
                "category":p.category,
            })
    return pd.DataFrame(rows)
def unique_categories_by_user(products_df:pd.DataFrame):
    return (products_df.groupby("user_name")["category"]
            .nunique()
            .reset_index()
            .rename(columns={"category":"unique_categories"}))
#43
def add_vip_column(products_df:pd.DataFrame):
    products_df=products_df.copy()
    products_df["VIP"]=products_df["total_sum"]>1000
    return products_df
#44
def sort_users(df:pd.DataFrame):
    return df.sort_values(
        by=["total_sum", "total_mean"],
        ascending=[False, True]
    ).reset_index(drop=True)
#45
def final_aggregated_report(merged_df: pd.DataFrame,
                            orders: list):
    total_orders = count_orders_by_user(merged_df)
    total_sum = group_orders_by_user(merged_df)
    mean_total = mean_order_by_user(merged_df)
    max_order = max_orders_by_user(merged_df)
    user_categories_df = orders_products_with_user(orders)
    unique_categories = unique_categories_by_user(user_categories_df)
    final_df = (
        total_orders
        .merge(total_sum, on="user_name")
        .merge(mean_total, on="user_name")
        .merge(max_order, on="user_name")
        .merge(unique_categories, on="user_name")
    )
    final_df = final_df.rename(columns={
        "orders_count": "total_orders",
        "total_mean": "total_mean"
    })
    final_df = add_vip_column(final_df)
    final_df = sort_users(final_df)
    return final_df


#1
u=User(1, "Lee Mark ","leemark@Example.COM")
print(u)
u2 = User.from_string("2, Eva James , evajames@wonder.com")
print(u2)
#3
p1=Product(1,"Laptop", 1200.0 ,"Electronics")
p2 = Product(2, "Phone",  799.0,  "Electronics")
p3 = Product(3, "Desk",     350.0, "Furniture")
p4 = Product(4, "Mouse",     25.0, "Electronics")
#4
inv=Inventory()
inv.add_product(p1)
inv.add_product(p2)
inv.add_product(p3)
inv.add_product(p4)
print("All products:")
print(p1)
print(p2)
print(p3)
print(p4)
print(inv.get_all_products())
print(inv.get_product(2))
print("Unique products:",len(inv.unique_products()))
print("to_dict keys:",list(inv.to_dict().keys()))
inv.remove_product(2)
print("after removing:",len(inv.get_all_products()))
expensive = inv.filter_by_price(300.0)
print("Products >= 300.0:",[p.name for p in expensive])
#6
logger = Logger()
logger.log_action(u, "purchase", p1, "log.txt")
logger.log_action(u, "view",     p2, "log.txt")
logger.log_action(u, "purchase", p2, "log.txt")
logs = logger.read_logs("log.txt")
for entry in logs:
    print(entry)
#7
order = Order(1,u)
order.add_product(p1)
order.add_product(p2)
order.add_product(p3)
print(order)
order.remove_product(2)
print(order)
print("Total:",order.total_price())
#8
print("Most expensive:")
for p in order.most_expensive_products(2):
    print(p)
#9
print("Price stream:")
for price in price_stream([p1,p2,p3]):
    print(price)
#10
order2=Order(2,u)
order2.add_product(p3)
order2.add_product(p4)
iterator = OrderIterator([order,order2])
print("order iterator")
for order in iterator:
    print(order)
#11
prices=get_price_array(inv.get_all_products())
print("Array:", prices)
#12
result=mean_median_price(prices)
print("Mean_Median_Price:", result)
#13
normalized=normalize_prices(prices)
print("Normalized:", normalized)
#14
categories=category_of_products(inv.get_all_products())
print("Categories:", categories)
#15
print("Unique categories:", count_unique_categories(categories))
#16
above_mean=products_above_mean(prices, inv.get_all_products())
print("Above_mean:",above_mean)
#17
sales=sales_price(prices)
print("Sales:", sales)
#18
order3=Order(1,u)
order3.add_product(p1)
order3.add_product(p2)
order4=Order(2,u2)
order4.add_product(p3)
order4.add_product(p4)
ordered=([order3,order4])
print("2D array:", orders_2d(ordered))
#19
avg=average_order_per_user(orders_2d(ordered))
print("Average order per user:",avg)
#20
indices=expensive_order_indices(orders_2d(ordered))
print("Expensive order indices:",indices)
#21
users=([u,u2])
df=users_to_dataframe(users)
print(df)
#22
products=([p1,p2,p3,p4])
df2=products_to_dataframe(products)
print(df2)
#23
users_df  = users_to_dataframe([u, u2])
orders_df = orders_to_dataframe([order3, order4])
print("Orders DF:")
print(orders_df)
merged = merge_users_orders(users_df, orders_df)
print("\nMerged DF:")
print(merged)
#24
print("Orders above 100:")
print(filter_orders_by_total(merged, 100.0))
print("\nOrders above 1000:")
print(filter_orders_by_total(merged, 1000.0))
#25
print(group_orders_by_user(merged))
#26
print(mean_order_by_user(merged))
#27
print(count_orders_by_user(merged))
#28
print(mean_price_by_category(df2))
#29
print(add_sale_price(df2))
#30
print(sort_products_by_price(df2))
#31
print(add_quantity(df2))
#32
res=(add_quantity(merged))
print(add_total_price(res))
#33
print(filter_by_category(df2,"Electronics"))
#34
print(count_products_by_category(df2))
#35
print(average_price_by_category(df2))
#36
res1=add_total_price(add_quantity(merged))
print(sort_orders_by_total(res1))
#37
print(top_n_orders(res1,3))
#38
users_df  = users_to_dataframe([u, u2])
orders_df = orders_to_dataframe([order3, order4])
merged = merge_users_orders(users_df, orders_df)
print(merged)
#39
print(mean_order_by_user(merged))
#40
print(count_orders_by_user(merged))
#41
print(max_orders_by_user(merged))
#42
df3=orders_products_with_user([order3,order4])
print(df3)
print(unique_categories_by_user(df3))
#43
grouped=group_orders_by_user(merged)
print(add_vip_column(grouped))
#44
grouped_sum  = group_orders_by_user(merged)
grouped_mean = mean_order_by_user(merged)
combined = pd.merge(grouped_sum, grouped_mean, on='user_name')
print(combined.columns.tolist())
print(combined)
print(sort_users(combined))
#45
final_df=final_aggregated_report(merged,ordered)
print(final_df)

app = FastAPI(title="Full OOP + NumPy + Pandas API")

users_list = [u, u2]
products_list = [p1, p2, p3, p4]
orders_list=[order3,order4]

@app.get("/")
def home():
    return {"message": "Project API is running"}

@app.get("/users")
def get_users():
    return [{"id": u._id, "name": u._name, "email": u._email} for u in users_list]

@app.get("/products")
def get_products():
    return [{"id": p.id, "name": p.name, "price": p.price, "category": p.category} for p in products_list]

@app.get("/orders")
def get_orders():
    return [
        {"order_id": o.id, "user": o.user._name, "total": o.total_price()}
        for o in ordered
    ]
@app.get("/user/str")
def user_str():
    return str(u)

@app.get("/user/from-string")
def user_from_string():
    return str(u2)

@app.get("/inventory/products")
def inventory_products():
    return [str(p) for p in inv.get_all_products()]

@app.get("/inventory/unique")
def inventory_unique():
    return len(inv.unique_products())

@app.get("/inventory/filter-price")
def inventory_filter():
    return [p.name for p in inv.filter_by_price(300.0)]

@app.get("/logs")
def logs():
    return logger.read_logs("log.txt")

@app.get("/order/summary")
def order_summary():
    return str(order)

@app.get("/order/expensive")
def order_expensive():
    return [str(p) for p in order.most_expensive_products(2)]

@app.get("/stream/prices")
def stream_prices():
    return list(price_stream([p1, p2, p3]))

@app.get("/orders/iterator")
def order_iterator():
    it = OrderIterator([order, order2])
    return [str(o) for o in it]

@app.get("/prices/array")
def prices_array():
    return get_price_array(inv.get_all_products()).tolist()

@app.get("/prices/mean-median")
def mean_median():
    return mean_median_price(get_price_array(inv.get_all_products()))

@app.get("/prices/normalize")
def normalize():
    return normalize_prices(get_price_array(inv.get_all_products())).tolist()

@app.get("/categories")
def categories():
    return category_of_products(inv.get_all_products()).tolist()

@app.get("/categories/unique")
def unique_categories():
    return count_unique_categories(category_of_products(inv.get_all_products()))

@app.get("/products/above-mean")
def above_mean():
    prices = get_price_array(inv.get_all_products())
    res = products_above_mean(prices, inv.get_all_products())
    return [p.name for p in res]

@app.get("/sales/prices")
def sales():
    return sales_price(get_price_array(inv.get_all_products())).tolist()

@app.get("/orders/2d")
def orders_2d_view():
    return orders_2d(orders_list).tolist()

@app.get("/orders/average")
def avg_orders():
    return average_order_per_user(orders_2d(orders_list))

@app.get("/orders/expensive-indices")
def expensive_indices():
    return expensive_order_indices(orders_2d(orders_list)).tolist()

@app.get("/df/users")
def df_users():
    return users_to_dataframe(users_list).to_dict(orient="records")

@app.get("/df/products")
def df_products():
    return products_to_dataframe(products_list).to_dict(orient="records")

@app.get("/df/orders")
def df_orders():
    users_df = users_to_dataframe(users_list)
    orders_df = orders_to_dataframe(orders_list)
    return merge_users_orders(users_df, orders_df).to_dict(orient="records")

@app.get("/df/orders/filter")
def filter_orders():
    users_df = users_to_dataframe(users_list)
    orders_df = orders_to_dataframe(orders_list)
    merged = merge_users_orders(users_df, orders_df)
    return filter_orders_by_total(merged, 100).to_dict()

@app.get("/df/group/user")
def group_user():
    users_df = users_to_dataframe(users_list)
    orders_df = orders_to_dataframe(orders_list)
    merged = merge_users_orders(users_df, orders_df)
    return group_orders_by_user(merged).to_dict()

@app.get("/df/mean/user")
def mean_user():
    users_df = users_to_dataframe(users_list)
    orders_df = orders_to_dataframe(orders_list)
    merged = merge_users_orders(users_df, orders_df)
    return mean_order_by_user(merged).to_dict()

@app.get("/df/count/user")
def count_user():
    users_df = users_to_dataframe(users_list)
    orders_df = orders_to_dataframe(orders_list)
    merged = merge_users_orders(users_df, orders_df)
    return count_orders_by_user(merged).to_dict()

@app.get("/df/category/mean-price")
def category_mean():
    return mean_price_by_category(products_to_dataframe(products_list)).to_dict()

@app.get("/df/products/sale")
def sale_price():
    return add_sale_price(products_to_dataframe(products_list)).to_dict()

@app.get("/df/products/sort")
def sort_products():
    return sort_products_by_price(products_to_dataframe(products_list)).to_dict()

@app.get("/df/orders/quantity")
def quantity():
    return add_quantity(orders_to_dataframe(orders_list)).to_dict()

@app.get("/df/orders/total")
def total_price():
    df = add_quantity(orders_to_dataframe(orders_list))
    return add_total_price(df).to_dict()

@app.get("/df/products/category")
def filter_category():
    return filter_by_category(products_to_dataframe(products_list), "Electronics").to_dict()

@app.get("/df/category/count")
def category_count():
    return count_products_by_category(products_to_dataframe(products_list)).to_dict()

@app.get("/df/category/avg")
def category_avg():
    return average_price_by_category(products_to_dataframe(products_list)).to_dict()

@app.get("/df/orders/sort")
def sort_orders():
    df = add_total_price(add_quantity(merge_users_orders(
        users_to_dataframe(users_list),
        orders_to_dataframe(orders_list)
    )))
    return sort_orders_by_total(df).to_dict()

@app.get("/df/orders/top")
def top_orders():
    df = add_total_price(add_quantity(merge_users_orders(
        users_to_dataframe(users_list),
        orders_to_dataframe(orders_list)
    )))
    return top_n_orders(df, 3).to_dict()

@app.get("/df/max-order")
def max_order():
    users_df = users_to_dataframe(users_list)
    orders_df = orders_to_dataframe(orders_list)
    merged = merge_users_orders(users_df, orders_df)
    return max_orders_by_user(merged).to_dict()

@app.get("/df/user/categories")
def user_categories():
    return unique_categories_by_user(orders_products_with_user(orders_list)).to_dict()

@app.get("/df/vip")
def vip():
    grouped = group_orders_by_user(merge_users_orders(
        users_to_dataframe(users_list),
        orders_to_dataframe(orders_list)
    ))
    return add_vip_column(grouped).to_dict()

@app.get("/df/sort-users")
def sort_users_api():
    grouped_sum = group_orders_by_user(merge_users_orders(
        users_to_dataframe(users_list),
        orders_to_dataframe(orders_list)
    ))
    grouped_mean = mean_order_by_user(merge_users_orders(
        users_to_dataframe(users_list),
        orders_to_dataframe(orders_list)
    ))

    combined = pd.merge(grouped_sum, grouped_mean, on="user_name")
    return sort_users(combined).to_dict()

@app.get("/report")
def final_report():
    users_df = users_to_dataframe(users_list)
    orders_df = orders_to_dataframe(orders_list)
    merged = merge_users_orders(users_df, orders_df)

    final_df = final_aggregated_report(merged, orders_list)

    return final_df.to_dict(orient="records")