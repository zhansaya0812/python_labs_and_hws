import json
orders=[
  {
    "order_id": 1,

    "user": "Ali",

    "items": ["phone", "case"],

    "total": 300000

  },
  {

    "order_id": 2,

    "user": "Dana",

    "items": ["laptop"],

    "total": 800000

  },
  {

    "order_id": 3,

    "user": "Ali",

    "items": ["mouse", "keyboard"],

    "total": 70000

  }
]
with open('orders.json', 'w') as file:
    json.dump(orders, file,indent=4, ensure_ascii=False)
with open('orders.json', 'r') as file:
    orders = json.load(file)
revenue=0
u_orders_count={}
t_items=0
frequency={}
max_price=-1
top_user=""
for order in orders:
    revenue+=order['total']
    user=order['user']
    u_orders_count[user]=u_orders_count.get(user,0)+1
    items=order['items']
    t_items+=len(items)
    for item in items:
      frequency[item]=frequency.get(item,0)+1
    if order['total']>max_price:
        max_price=order['total']
        top_user=user
popular_item=max(frequency,key=frequency.get,default="no items")
result={
    "revenue":revenue,
    "top_user":top_user,
    "popular_item":popular_item,
    "orders":len(orders)
}
with open('result.json', 'w', encoding='utf-8') as file:
    json.dump(result, file,indent=4,ensure_ascii=False)
print("json file is ready")