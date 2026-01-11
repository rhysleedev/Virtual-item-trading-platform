class Item:
    def __init__(self,item_id,name,price,type="Generic",rarity="Common"):
        self.item_id=item_id
        self.name=name
        self.price=price
        self.type=type
        self.rarity=rarity

    def __repr__(self):
        return f"{self.name} ({self.type}, {self.rarity}, ${self.price})"

class Player:
    def __init__(self,player_id,username,balance=100,level=1,xp=0,inventory=None):
        if inventory is None:
            inventory=[]
        self.player_id=player_id
        self.username=username
        self.balance=balance
        self.level=level
        self.xp=xp
        self.inventory=inventory

    def add_item(self,item):
        self.inventory.append(item)
        self.gain_xp(10)

    def remove_item(self,item):
        self.inventory.remove(item)

    def gain_xp(self,amount):
        self.xp+=amount
        while self.xp>=100:
            self.xp-=100
            self.level+=1
            print(f"{self.username} leveled up to {self.level}!")

    def __repr__(self):
        return f"{self.username}, Balance: ${self.balance}, (Level {self.level}, XP: {self.xp})"
