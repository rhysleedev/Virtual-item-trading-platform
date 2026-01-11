from models import Player,Item
from exceptions import *

class TradingService:
    def __init__(self):
        self.players={}
        self.items={}

    def create_player(self,player_id,username):
        self.players[player_id]=Player(player_id,username)

    def get_player(self,player_id):
        if player_id not in self.players:
            print(f"ERROR: {player_id} does not exist")
        return self.players[player_id]

    def create_item(self,item_id,name,price,type="Generic",rarity="Common"):
        self.items[item_id]=Item(item_id,name,price,type,rarity)

    def get_item(self,item_id):
        if item_id not in self.items:
            print(f"ERROR: {item_id} does not exist")
        return self.items[item_id]

    def buy_item(self,player_id,item_id):
        player=self.get_player(player_id)
        item=self.get_item(item_id)

        if player.balance<item.price:
            print(f"ERROR: {player.username} attempted to buy {item.name} but does not have enough balance")
        else:
            player.balance-=item.price
            player.add_item(item)

    def sell_item(self,player_id,item_id,sell_price=None):
        player=self.get_player(player_id)
        item=self.get_item(item_id)

        if item not in player.inventory:
            print(f"ERROR: {player.username} does not own {item.name}")        
        else:
            player.remove_item(item)
            player.balance+=sell_price or (item.price//2)

    def trade_item(self,from_player_id,to_player_id,item_id):
        from_player=self.get_player(from_player_id)
        to_player=self.get_player(to_player_id)
        item=self.get_item(item_id)

        if item not in from_player.inventory:
            print(f"ERROR: {player.username} does not own {item.name}")
        else:
            from_player.remove_item(item)
            to_player.add_item(item)

