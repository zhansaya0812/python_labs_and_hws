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



