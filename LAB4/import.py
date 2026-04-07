from flask import Flask,jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger=Swagger(app)

@app.route('/sum')
def function():
    a=1
    b=2
    return str(a+b)
@app.route('/')
def home():
    return "Сервер жұмыс істеп тұр"
if __name__ == '__main__':
    app.run(port=5002)

from fastapi import FastAPI
from datetime import datetime
import random
app = FastAPI()
# 1,2,16,17
class Player:
    def __init__(self, player_id: int, name: str, hp: int):
        self._id = player_id
        self._name = name.strip().title()
        self._hp = hp if hp >= 0 else 0
        self._inventory = Inventory()

    def __str__(self):
        return f"Player(id={self._id}, name='{self._name}', hp={self._hp})"

    def __del__(self):
        print(f"Player {self._name} удалён")

    @classmethod
    def from_string(cls, data: str):
        try:
            parts = data.strip().split(",")
            if len(parts) != 3:
                raise ValueError()

            return cls(int(parts[0]), parts[1], int(parts[2]))
        except:
            raise ValueError("Ошибка строки")


    @property
    def hp(self):
        return self._hp

    def change_hp(self, value):
        self._hp = max(0, self._hp + value)

    def get_inventory(self):
        return self._inventory



#3
class Item:
    def __init__(self, item_id: int, name: str, power: int):
        self.id = item_id
        self.name = name.strip()
        self.power = power
    def __str__(self):
        return f"Item(id={self.id}, name='{self.name}', power={self.power})"
    def __eq__(self, other):
        return isinstance(other,Item) and self.id == other.id
    def __hash__(self):
        return hash(self.id)

#4
class Inventory:
    def __init__(self):
        self.items = []
    def add_item(self, item: Item):
        if not any(i.id == item.id for i in self.items):
            self.items.append(item)
    def remove_item(self, item_if: int):
        self.items = [i for i in self.items if i.id != item.id]
    def get_items(self):
        return self.items
    def unique_items(self):
        return set(self.items)
    def to_dict(self):
        return {item.id: item for item in self.items}

#5
def get_strong_items(self, min_power):
    return list(filter(lambda x: x.power >= min_power, self.items))

#6
class Event:
    def __init__(self, type_, data):
        self.type = type_
        self.data = data
        self.timesmap = datetime.now()
    def __str__(self):
        return f"Event(type='{self.type}', data={self.data}, timestamp='{self.timestamp}')"

#7
    def handle_event(self, event):
        if event.type == "ATTACK":
            damage = event_hp(-damage)
            self.change_hp(-damage)
        elif event.type == "HEAL":
            heal = event.data.get("heal", 0)
            self.change_hp(heal)
        elif event.type == "LOOT":
            item = event.data.get("item")
            if item:
                self._inventory.add_item(item)

#8
class Logger:
    @staticmethod
    def log(event, player, filename):
        with open(filename, "a") as f:
            f.write(f"{event.timestamp};{player._id};{event.type};{event.data}\n")

#9
    @staticmethod
    def read_logs(filename):
        events = []
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split(";")
                e = Event(parts[2], eval(parts[3]))
                events.append(e)
        return events

#10
class EventIterator:
    def __init__(self, events):
        self.events = events
        self.index = 0
    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.events):
            raise StopIteration
        val = self.events[self.index]
        self.index += 1
        return val

#11
def damage_stream(events):
    for e in events:
        if e.type == "ATTACK":
            yield e.data.get("damage", 0)

#12
def generate_events(players, items, n):
    types = ["ATTACK", "HEAL", "LOOT"]

    events = []
    for _ in range(n):
        for p in players:
            t = (lambda x: random.choice(x))(types)

            if t == "ATTACK":
                events.append(Event(t, {"damage": random.randint(5, 20)}))

            elif t == "HEAL":
                events.append(Event(t, {"heal": random.randint(5, 15)}))

            else:
                events.append(Event(t,