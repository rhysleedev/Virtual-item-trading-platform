from service import TradingService
from models import Player, Item

def main():
    service=TradingService()

    #create players
    service.create_player(1,"Alice")
    service.create_player(2,"Bob")
    service.create_player(3,"Charlie")

    #create items
    service.create_item(101,"Sword of Vengeance",50, type="Weapon",rarity="Epic")
    service.create_item(102,"Shield of Light",40, type="Armour", rarity="Rare")
    service.create_item(103,"Potion of Healing", 20, type="Potion", rarity="Common")
    service.create_item(104,"Bow of Accuracy",60, type="Weapon", rarity="Rare")
    service.create_item(105,"Ring of Wisdom",80, type="Accessory", rarity="Epic")

    #buying items
    service.buy_item(1,101)
    service.buy_item(1,103)
    service.buy_item(2,102)
    service.buy_item(3,104)
    service.buy_item(3,105)

    #trades
    service.trade_item(1,2,103)
    service.trade_item(3,1,104)

    #selling items
    service.sell_item(2,103)

    #print player info
    print("\n---Players & Inventories---")
    for player_id in service.players:
        player=service.get_player(player_id)
        print(f"\n{player}")
        inventory_list=[f"{item.name} ({item.type}, {item.rarity})" for  item in player.inventory]
        print(f"Inventory: {inventory_list}")
        print(f"Balance: ${player.balance}")

if __name__=="__main__":
    main()