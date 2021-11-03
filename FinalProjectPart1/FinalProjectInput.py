# Michael Rupert
# 1855121

import csv
from datetime import date

current_date = date.today().strftime("%m/%d/%y")




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
with open('ManufacturerList(3).csv') as manu_list_csv:
    csv_reader = csv.reader(manu_list_csv, delimiter=',')
    line_count = 0
    for row in csv_reader:
        list_manu_objs.append(Manufacturer_List(row[0], row[1], row[2], row[3]))

with open('PriceList(1).csv') as price_list_csv:
    csv_reader = csv.reader(price_list_csv, delimiter=',')
    line_count = 0
    for row in csv_reader:
        list_price_objs.append(Price_List(row[0], row[1]))

with open('ServiceDatesList(3).csv') as servdata_list_csv:
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

with open("FullInventory.csv", 'w') as f:
    writer = csv.writer(f)

    # write the data
    writer.writerows(list(list_fullinventory_objs))

item_types = []

for manu_obj in list_manu_objs:
    item_types.append(manu_obj.item_type)

item_types = set(item_types)

for item_type in item_types:
    with open("C:\\Users\\micha\\PycharmProjects\\ProjectPt1\\" + item_type + ".csv", 'w') as f:
        writer = csv.writer(f)
        inv_list = []

        # write the data
        for full_inv in list_fullinventory_objs:
            if full_inv.item_type == item_type:
                inv_list.append(full_inv)

        inv_list.sort(key=lambda x: x.item_ID)

        writer.writerows(list(inv_list))

#for items past thier service dates
past_date_items = []
for full_inv in list_fullinventory_objs:
    if full_inv.serv_date > current_date:
        past_date_items.append(full_inv)

past_date_items.sort(key=lambda x: x.serv_date, reverse=True)

with open("C:\\Users\\micha\\PycharmProjects\\ProjectPt1\\PastServiceDateInventory.csv", 'w') as f:
    writer = csv.writer(f)

    # write the data
    writer.writerows(list(past_date_items))

#items damaged
damaged_items = []
for full_inv in list_fullinventory_objs:
    if full_inv.damaged != '':
        damaged_items.append(full_inv)

damaged_items.sort(key=lambda x: x.item_price, reverse=True)

with open("C:\\Users\\micha\\PycharmProjects\\ProjectPt1\\DamagedInventory.csv", 'w') as f:
    writer = csv.writer(f)

    # write the data
    writer.writerows(list(damaged_items))
