#Program working with a game inventory
#Two functions to display inventory and add item drops into the inventory and reprint

inventory = {"rope": 1, "torch":6, "gold coin": 42, "dagger": 1, "arrow": 12}
drops = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]

def displayInventory(inventory): 
    print("Inventory:")
    totalItemCount = 0
    for item, count in inventory.items():
        print(str(count) + " " + item)
        totalItemCount = count + totalItemCount
    print("Total number of items: " + str(totalItemCount))

def itemDrops(inventory, drops):
    print(" ")
    for x in range(len(drops)):
        inventory.setdefault(drops[x], 0)
        inventory[drops[x]] = inventory[drops[x]] + 1
    return inventory

displayInventory(inventory)
inventory = itemDrops(inventory,drops)
displayInventory(inventory)
