import os

from WonderlandsSave import WonderlandsSave
from Items import Items

if __name__ == '__main__':
    db = Items()
    db.load('gun_balances.csv', "GUNS")
    db.load('shield_balances.csv', "SHIELDS")
    db.load('com_balances.csv', "PAULDRONS")
    db.load('spell_balances.csv', "SPELLS")
    db.load('ring_balances.csv', "RINGS")
    db.load('amulet_balances.csv', "AMULETS")
    db.load('melee_balances.csv', "MELEE")

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    save_a = WonderlandsSave(os.path.join(__location__, "80_blues.sav"))
    items = save_a.get_items()
    for item in items:
        balance = item.balance
        # if "Repellant" in item.balance_short:
        #     print("ok")
        all_parts = db.get_parts(item.balance_short)
        if not all_parts:
            print("--- No data about {}".format(item.balance_short))
            continue
        is_legit = db.is_legit(item)
        if is_legit:
            print("{} is legit".format(item.balance_short))
        else:
            print("--------------------------------> {} is not legit <--------------------------------".format(item.balance_short))
