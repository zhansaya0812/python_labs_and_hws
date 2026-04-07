# AI Dungeon Game Log System
#1
from fastapi import FastAPI
from datetime import datetime
import uvicorn
from typing_extensions import type_repr

app = FastAPI()

class Player:
    def __init__(self, _id, name, hp):
        self._id = _id
        self._name = name.strip().title()
        self._hp = hp if hp >= 0 else 0
        self._inventory= Inventory()

    def __str__(self):
        return f"Player(id={self._id}, name='{self._name}', hp={self._hp})"

    @classmethod
    def from_string(cls, data: str):
        parts = data.strip().split(",")
        if len(parts) != 3:
            raise ValueError()
        return cls(int(parts[0]), parts[1], int(parts[2]))
        except:
            raise ValueError("Ошибка строки")

    @property
    def hp(self):
        return self._hp
    def change_hp(self,value):
        self._hp=max(0,self._hp+value)
    def get_inventory(self):
        return self._inventory

        _id = int(parts[0].strip())
        name = parts[1].strip()
        hp = int(parts[2].strip())

        return cls(_id, name, hp)

#3
class Item:
    def __init__(self, item_id:int, name:str,power:int ):
        self.id = item_id
        self.name = name.strip()
        self.power = power
    def __str__(self):
        return f"Item(id={self.id}, name='{self.name}', power={self.power})"
    def __eq__(self, other):
        return isinstance(other, Item) and self.id == other.id
    def __hash__(self):
        return hash(self.id)
#4
class Inventory:
    def __init__(self):
        self.items = []
    def add_item(self, item:Item):
        if not any(i.id == item.id for i in self.items):
            self.items.append(item)
    def get_items(self):
        return self.items
    def unique_items(self):
        return set(self.items)
    def to_dict(self):
        return {item.id:item for item in self.items}
#5
def get_strong_items(self,min_power):
    return list(filter(lambda x: x.power >= min_power,self.items))
#6
class Event:
    def __init__(self,type,data):
        self.type = type_
        self.data = data
        self.timesmap=datetime.now()
    def __str__(self):
        return f"Event(type='{self.type}', data={self.data},timesmap='{self.timesmap}')"
#7
    def handle_event(self,event):
        if event.type=="ATTACK":
            damage=event_hp(-damage)
            self.change_hp(-damage)
        elif event.type=="HEAL":
            heal=event.data.get("heal",0)
            self.change_hp(heal)
        elif event.type=="LOOT":
            item=event.data.get("item")
            if item:
                self._inventory.add_item(item)
#8
class Logger:
    @staticmethod
    def log(event,player,filename):
        with open(filename,"a") as f:
            f.write(f"{event.timestamp};{player._id};{event.type};{event.data}\n")
#9
    @staticmethod
    def read_logs(filename):
        events = []
        with open(filename,"r") as f:
            for line in f:
                parts= line.strip().split(";")
                e=Event(parts[2],eval(parts[3]))
                events.append(e)
        return events
#10
class EventHandler:
    def __init__(self,events):
        self.events = events
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.events):
            raise StopIteration
        value = self.events[self.index]
        self.index += 1
        return value
#11
def damage_stream(events):
    for e in events:
        if e.type=="ATTACK":
            yield e.data.get("damage",0)
#12

            _






@app.get("/players")
def get_players():
    p1 = Player(1, " john ", 120)
    p2 = Player.from_string("2, alice , 90")

    return {
        "players": [
            str(p1),
            str(p2)
        ]
    }

