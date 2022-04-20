import csv


class Items:
    def __init__(self):
        self.items = {}

    def load(self, filename, type):
        with open(filename, newline='\n') as file:
            reader = csv.reader(file, delimiter=',')
            header = next(reader)
            for row in reader:
                self.add(row, type)

    def add(self, row, type):
        item = Item(row, type)
        if not self.items.get(item.balance, None):
            self.items[item.balance] = []
        self.items[item.balance].append(item)

    def get_parts(self, balance):
        ret = {}
        for elm in self.items.get(balance, []):
            if not ret.get(elm.category, None):
                ret[elm.category] = []
            ret[elm.category].append(elm)
        return ret

    def get_category(self, item, part):
        for elm in self.items.get(item.balance_short, []):
            if elm.parts == part:
                return elm.category

    def is_in_category(self, item, part, category):
        all_parts = self.get_parts(item.balance_short)
        parts = all_parts.get(category, [])
        for elm in parts:
            if elm.parts == part:
                return True
        return False

    def get_min_max(self, item, category):
        all_parts = self.get_parts(item.balance_short)
        part = all_parts[category][0]
        return part.min_parts, part.max_parts

    def is_legit(self, item):
        item_parts = item.parts
        counts = {}
        for part, id in item_parts:
            part_name = part.split('.')[-1]
            cat = self.get_category(item, part_name)
            good = self.is_in_category(item, part_name, cat)
            if good:
                if not counts.get(cat, None):
                    counts[cat] = 0
                counts[cat] = counts[cat] + 1

        for key, value in counts.items():
            min, max = self.get_min_max(item, key)
            if value < min or value > max:
                return False

        return True

class Item:
    def __init__(self, row, type):
        if type == "GUNS":
            self.manufacturer = row[0]
            self.gun_type = row[1]
            self.rarity = row[2]
            self.balance = row[3].split('\\')[-1]
            self.category = row[4]
            self.min_parts = int(row[5])
            self.max_parts = int(row[6])
            self.weight = float(row[7])
            self.parts = row[8] if row[8] != "None" else None
            self.dependencies = row[9].split(',') if row[9] != "" else []
            self.excluders = row[10].split(',') if row[10] != "" else []
        elif type == "SHIELDS":
            self.manufacturer = row[0]
            self.rarity = row[1]
            self.balance = row[2].split('\\')[-1]
            self.category = row[3]
            self.min_parts = int(row[4])
            self.max_parts = int(row[5])
            self.weight = float(row[6])
            self.parts = row[7] if row[7] != "None" else None
            self.dependencies = row[8].split(',') if row[8] != "" else []
            self.excluders = row[9].split(',') if row[9] != "" else []
        elif type == "PAULDRONS":
            self.manufacturer = row[0]
            self.rarity = row[1]
            self.balance = row[2].split('\\')[-1]
            self.category = row[3]
            self.min_parts = int(row[4])
            self.max_parts = int(row[5])
            self.weight = float(row[6])
            self.parts = row[7] if row[7] != "None" else None
            self.dependencies = row[8].split(',') if row[8] != "" else []
            self.excluders = row[9].split(',') if row[9] != "" else []
        elif type == 'SPELLS':
            self.name = row[0]
            self.type = row[1]
            self.rarity = row[2]
            self.balance = row[3].split('\\')[-1]
            self.category = row[4]
            self.min_parts = int(row[5])
            self.max_parts = int(row[6])
            self.weight = float(row[7])
            self.parts = row[8] if row[8] != "None" else None
            self.dependencies = row[9].split(',') if row[9] != "" else []
            self.excluders = row[10].split(',') if row[10] != "" else []
        elif type == 'RINGS':
            self.name = row[0]
            self.type = row[1]
            self.rarity = row[2]
            self.balance = row[3].split('\\')[-1]
            self.category = row[4]
            self.min_parts = int(row[5])
            self.max_parts = int(row[6])
            self.weight = float(row[7])
            self.parts = row[8] if row[8] != "None" else None
            self.dependencies = row[9].split(',') if row[9] != "" else []
            self.excluders = row[10].split(',') if row[10] != "" else []
        elif type == 'MELEE':
            self.name = row[0]
            self.type = row[1]
            self.rarity = row[2]
            self.balance = row[3].split('\\')[-1]
            self.category = row[4]
            self.min_parts = int(row[5])
            self.max_parts = int(row[6])
            self.weight = float(row[7])
            self.parts = row[8] if row[8] != "None" else None
            self.dependencies = row[9].split(',') if row[9] != "" else []
            self.excluders = row[10].split(',') if row[10] != "" else []
        else:
            self.manufacturer = row[0]
            self.rarity = row[1]
            self.balance = row[2].split('\\')[-1]
            self.category = row[3]
            self.min_parts = int(row[4])
            self.max_parts = int(row[5])
            self.weight = float(row[6])
            self.parts = row[7] if row[7] != "None" else None
            self.dependencies = row[8].split(',') if row[8] != "" else []
            self.excluders = row[9].split(',') if row[9] != "" else []

