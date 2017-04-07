import copy


def main():
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    display_inventory(stuff)

    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    new_inv = add_to_inventory(inv, dragonLoot)
    display_inventory(new_inv)


def display_inventory(inventory):
    print("Inventory: ")
    item_total = 0
    for k, v in inventory.items():
        print("{} {}".format(v, k))
        item_total += v
    print("Total number of items: {}".format(item_total))


def add_to_inventory(inventory, addedItems):
    added_inv = copy.copy(inventory)
    for item in addedItems:
        added_inv.setdefault(item, 1)
    return added_inv


if __name__ == "__main__":
    main()