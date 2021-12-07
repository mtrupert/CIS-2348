#Michael Rupert
#1855121

import csv
from datetime import date

current_date = date.today().strftime("%m/%d/%Y")


class Manufacturer_List:
    def __init__(self, item_ID, manu_name, item_type, damaged):
        self.item_ID = item_ID
        self.manu_name = manu_name
        self.item_type = item_type
        self.damaged = damaged

    def manufacture_list_data(self):
        print('Item ID:', self.item_ID)
        print('Manufacturer Name:', self.manu_name)
        print('Type:', self.item_type)
        print('Damaged:', self.damaged)


class Price_List:
    def __init__(self, item_ID, item_price):
        self.item_ID = item_ID
        self.item_price = item_price

    def price_list_data(self):
        print('Item ID:', self.item_ID)
        print('Item Price:', self.item_price)


class ServiceDate_List:
    def __init__(self, item_ID, serv_date):
        self.item_ID = item_ID
        self.serv_date = serv_date

    def servicedata_list_data(self):
        print('Item ID:', self.item_ID)
        print('Service Date:', self.serv_date)


class FullInventory:
    def __init__(self, item_ID, manu_name, item_type, item_price, serv_date, damaged):
        self.item_ID = item_ID
        self.manu_name = manu_name
        self.item_type = item_type
        self.item_price = item_price
        self.serv_date = serv_date
        self.damaged = damaged

    def __iter__(self):
        return iter([self.item_ID, self.manu_name, self.item_type, self.item_price, self.serv_date, self.damaged])

    def full_inventory_data(self):
        print('Item ID:', self.item_ID)
        print('Manufacturer Name:', self.manu_name)
        print('Type:', self.item_type)
        print('Item Price:', self.item_price)
        print('Service Date:', self.serv_date)
        print('Damaged:', self.damaged)


list_manu_objs = []
list_price_objs = []
list_servicedata_objs = []
list_fullinventory_objs = []

# populating objects with data from CSV
with open("ManufacturerList4.csv") as manu_list_csv:
    csv_reader = csv.reader(manu_list_csv, delimiter=',')
    line_count = 0
    for row in csv_reader:
        list_manu_objs.append(Manufacturer_List(row[0], row[1], row[2], row[3]))

with open("PriceList2.csv") as price_list_csv:
    csv_reader = csv.reader(price_list_csv, delimiter=',')
    line_count = 0
    for row in csv_reader:
        list_price_objs.append(Price_List(row[0], row[1]))

with open("ServiceDatesList4.csv") as servdata_list_csv:
    csv_reader = csv.reader(servdata_list_csv, delimiter=',')
    line_count = 0
    for row in csv_reader:
        list_servicedata_objs.append(ServiceDate_List(row[0], row[1]))

# making FullInventory.csv
for manu_obj in list_manu_objs:
    for plist_obj in list_price_objs:
        for sdlist_obj in list_servicedata_objs:
            if manu_obj.item_ID == plist_obj.item_ID and manu_obj.item_ID == sdlist_obj.item_ID:
                list_fullinventory_objs.append(
                    FullInventory(manu_obj.item_ID, manu_obj.manu_name, manu_obj.item_type, plist_obj.item_price,
                                  sdlist_obj.serv_date, manu_obj.damaged))

# Sorting fullinventory based on Name
list_fullinventory_objs.sort(key=lambda x: x.manu_name)

with open("C:\\Users\\micha\\PycharmProjects\\ProjectPt1\\FullInventory.csv", 'w') as f:
    writer = csv.writer(f)

    # write the data
    writer.writerows(list(list_fullinventory_objs))

# making a list with distinct manu names and item types
manu_names = []
item_types = []
for i in list_manu_objs:
    manu_names.append(i.manu_name.strip())
    item_types.append(i.item_type.strip())
manu_names = list(set(manu_names))
item_types = list(set(item_types))


def manu_item_search(manu_type_input):
    name_found = False
    type_found = False

    item_manu_name = ""
    item_type = ""

    found_items = []
    same_item_diff_manu = []

    for i in manu_type_input:
        if (i in map(str.lower, manu_names)):
            name_found = True
            item_manu_name = i
        if (i in map(str.lower, item_types)):
            type_found = True
            item_type = i
    print(manu_names)
    if (not (name_found and type_found)):
        print("\nNo such item in inventory")
        return

    elif (name_found and type_found):
        print(item_manu_name + " " + item_type)
        found_items = contains_manu_item(item_manu_name, item_type)

    if (len(found_items) == 0):
        print("\nNo such item in inventory")
        return

    elif (len(found_items) >= 1):
        # print("found: " + str(len(found_items)))
        print("\nYour item is: ")
        found_items[0].full_inventory_data()

    same_item_diff_manu = find_same_item_diff_manu(item_manu_name, item_type)
    if (len(same_item_diff_manu) == 0):
        return

    elif (len(same_item_diff_manu) == 1):
        print("\nYou may also consider: ")
        same_item_diff_manu[0].full_inventory_data()

    elif (len(same_item_diff_manu) > 1):
        diff = []
        index = -1
        item_price = found_items[0].item_price
        for i in same_item_diff_manu:
            diff.append(abs(found_items[0].item_price - i.item_price))
        index = diff.index(min(diff))

        print("\nYou may also consider: " + same_item_diff_manu[index].full_inventory_data())


def contains_manu_item(item_manu_name, item_type):
    found = False
    found_items = []
    for i in list_fullinventory_objs:
        if (
                i.manu_name.strip().lower() == item_manu_name.lower() and i.item_type.lower() == item_type.lower() and current_date < i.serv_date and len(
                i.damaged) == 0):
            found_items.append(i)

    found_items.sort(key=lambda x: x.item_price, reverse=True)
    return found_items


def find_same_item_diff_manu(item_manu_name, item_type):
    found_items = []
    for i in list_fullinventory_objs:
        if (
                i.manu_name.strip().lower() != item_manu_name.lower() and i.item_type.lower() == item_type.lower() and current_date < i.serv_date and len(
                i.damaged) == 0):
            found_items.append(i)

    return found_items


# ask user for manufacture and item type and store in String list form
choice = ''
while (choice != 'q' and choice != 'Q'):
    print("\nPlease enter Item Manufacturer and Type: ")
    manu_type_input = input().strip().split(" ")
    print(manu_type_input)
    manu_item_search(manu_type_input)
    print("\nContinue? (Press any key to continue or Q to Quit): ")
    choice = input().strip()

print("\nProgram has finished execution")