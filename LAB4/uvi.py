# #1 & #16, #17
from fastapi import FastAPI, HTTPException
from datetime import datetime
import ast
import random
from collections import Counter
from typing import Iterator

app = FastAPI(title="AI Dungeon Game Log System")


# #3
class Item:

    def __init__(self, item_id: int, name: str, power: int):
        self.id = item_id
        self.name = name.strip().title()
        self.power = power

    def __str__(self):
        return f"Item(id={self.id}, name='{self.name}', power={self.power})"

    def __eq__(self, other):
        return isinstance(other, Item) and self.id == other.id

    def __hash__(self):
        return hash(self.id)


# #4 & #18
class Inventory:

    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        if not any(i.id == item.id for i in self.items):
            self.items.append(item)

    def remove_item(self, item_id: int):
        self.items = [i for i in self.items if i.id != item_id]

    def get_items(self):
        return self.items

    def unique_items(self):
        return set(self.items)

    def to_dict(self):
        return {item.id: item for item in self.items}

    # #5
    def get_strong_items(self, min_power: int):
        return [item for item in self.items if item.power >= min_power]

    def __iter__(self):
        return iter(self.items)


# #6
class Event:

    def __init__(self, type: str, data: dict):
        self.type = type
        self.data = data
        self.timestamp = datetime.now()

    def __str__(self):
        ts = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        return f"Event(type='{self.type}', data={self.data}, timestamp='{ts}')"


# #1, #2, #7, #15 (объединён Player)
class Player:

    def __init__(self, _id, name, hp):
        self._id = _id
        self._name = name.strip().title()
        self._hp = max(0, hp)
        self._inventory = Inventory()

    def __str__(self):
        return f"Player(id={self._id}, name='{self._name}', hp={self._hp})"

    def __del__(self):
        print(f"Player {self._name} удалён")

    # #2
    @classmethod
    def from_string(cls, data: str):

        parts = data.split(",")

        if len(parts) != 3:
            raise ValueError("Неверный формат")

        id_str, name_str, hp_str = parts

        player_id = int(id_str.strip())
        hp = int(hp_str.strip())

        return cls(player_id, name_str.strip(), hp)

    # #7 & #15
    def change_hp(self, amount: int):
        self._hp = max(0, self._hp + amount)

    def handle_event(self, event):

        if event.type == "ATTACK":
            damage = event.data.get("damage", 0)
            self.change_hp(-damage)

        elif event.type == "HEAL":
            heal = event.data.get("heal", 0)
            self.change_hp(heal)

        elif event.type == "LOOT":
            item = event.data.get("item")

            if item:
                self._inventory.add_item(item)

    @property
    def hp(self):
        return self._hp

    @property
    def inventory(self):
        return self._inventory


# #7
class Warrior(Player):

    def handle_event(self, event: Event):

        if event.type == "ATTACK":
            damage = event.data.get("damage", 0)
            self.change_hp(-damage)

        else:
            super().handle_event(event)


class Mage(Player):

    def handle_event(self, event: Event):

        if event.type == "LOOT":

            item = event.data.get("item")

            if item:
                item.power = int(item.power * 1.1)
                self._inventory.add_item(item)

        else:
            super().handle_event(event)


# #8
class Logger:

    @staticmethod
    def log(event, player, filename):

        ts = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")

        line = f"{ts};{player._id};{event.type};{event.data}\n"

        with open(filename, "a", encoding="utf-8") as f:
            f.write(line)


# #9
    @staticmethod
    def read_logs(filename: str):

        events = []

        with open(filename, "r", encoding="utf-8") as f:

            for line in f:

                parts = line.strip().split(";")

                if len(parts) != 4:
                    continue

                timestamp_str, player_id, event_type, data_str = parts

                e = Event(
                    event_type,
                    ast.literal_eval(data_str)
                )

                events.append(e)

        return events


# #10
class EventIterator:

    def __init__(self, events):
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


# #11
def damage_stream(events):

    for event in events:

        if event.type == "ATTACK":
            yield event.data.get("damage", 0)


# #12
def generate_events(players,items,n):
    types=["ATTACK","HEAL","LOOT"]
    events=[]
    for player in players:
        for _ in range(n):
            t=random.choice(types)
            if t =="ATTACK":
                data={"damage":random.randint(5,20)}
            elif t == "HEAL":
                data={"heal":random.randint(5,15)}
            else:
                data={"item":random.choice(items)}
            events.append(Event(t, data))
    return events

# #13
def analyze_logs(events):
    total_damage=sum(e.data.get("damage", 0) for e in events if e.type == "ATTACK")
    most_common=Counter(e.type for e in events).most_common(1)
    player_damage={
        name:sum(e.data.get("damage",0) for e in events if e.data.get("player_name")==name)
        for name in {e.data.get("player_name") for e in events if "player_name" in e.data}
    }
    return {
        "total_damage":total_damage,
        "top_player":max(player_damage,key=player_damage.get) if player_damage else None,
        "most_common_event":Counter(e.type for e in events).most_common(1)[0][0] if events else None
    }
# #14
decide_action = lambda hp, inventory: (
    "HEAL" if hp < 20
    else "ATTACK" if len(inventory) >= 3
    else "LOOT"
)


# #19
def analyze_inventory(inventories):

    all_unique_items = {
        item
        for inv in inventories
        for item in inv
    }

    top_power_item = max(
        all_unique_items,
        key=lambda item: item.power
    ) if all_unique_items else None

    return {
        "unique_items": all_unique_items,
        "top_power_item": top_power_item
    }


# #20 DATABASE
players_db = [
    Warrior(1, "Jimmy", 100),
    Mage(2, "Katy", 80)
]

items_db = [
    Item(1, "Frostmourne", 100),
    Item(2, "Staff", 50)
]


# HTTP API


@app.get("/")
def read_root():
    return {"message": "RPG API works! Go to /docs for testing"}


@app.get("/status")
def get_world_status():

    return [
        {
            "id": p._id,
            "name": p._name,
            "hp": p.hp,
            "items_count": len(p.inventory.get_items())
        }

        for p in players_db
    ]


@app.post("/simulate/{n}")
def run_simulation(n: int):

    if n <= 0:

        raise HTTPException(
            status_code=400,
            detail="Количество событий должно быть > 0"
        )

    new_events = generate_events(
        players_db,
        items_db,
        n
    )

    for event in new_events:

        player = random.choice(players_db)

        player.handle_event(event)

    return {
        "status": "success",
        "processed_events": len(new_events)
    }


@app.get("/analytics")
def get_analytics():

    top_hp_player = max(
        players_db,
        key=lambda p: p.hp
    )

    return {
        "healthiest_player": top_hp_player._name,
        "total_players": len(players_db)
    }