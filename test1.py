# encoding:utf-8
import json
import csv
Character = json.load(open("character.json", "r"))
Item_Talents = json.load(open("item_Talents.json", "r"))
Item_Nor = json.load(open("item_Nor.json", "r"))
Item_Weekly = json.load(open("item_Weekly.json", "r"))
Csvlist = list(csv.reader(open('.Talents.csv', "r")))
Needs = json.load(open("needs.json", "r"))
Part = False


def list_talents(name):
    reslut = [Item_Talents[Character[name]["天赋材料"]]["0"],
              Item_Talents[Character[name]["天赋材料"]]["1"],
              Item_Talents[Character[name]["天赋材料"]]["2"],
              Item_Nor[Character[name]["普通材料"]]["0"],
              Item_Nor[Character[name]["普通材料"]]["1"],
              Item_Nor[Character[name]["普通材料"]]["2"],
              Item_Weekly[Character[name]["周常材料"]]["0"],
              "智识之冕",
              "摩拉"]
    return reslut


Cha_name = []
List = []
for key in Needs.keys():
    Cha_name.append(key)
for name in Cha_name:
    Cha_Tal_1 = []
    Cha_Tal_1_s = Needs[name]["1技能初始"]
    while Cha_Tal_1_s <= Needs[name]["1技能目标"]:
        Cha_Tal_1.append(Cha_Tal_1_s)
        Cha_Tal_1_s += 1
    List_Talents_1 = []
    for lv in Cha_Tal_1:
        Csvlist[lv-1] = list(map(int, Csvlist[lv-1]))
        List_Talents = list_talents(name)
        Dict_Talents_1 = dict(zip(List_Talents, Csvlist[lv-1]))
        List_Talents_1.append(Dict_Talents_1)
    n = 0
    Dict_Talents_1_item = {}
    while n <= len(List_Talents_1)-1:
        for key in list(Dict_Talents_1_item | List_Talents_1[n]):
            if Dict_Talents_1_item.get(key) and List_Talents_1[n].get(key):
                Dict_Talents_1_item.update(
                    {key: Dict_Talents_1_item.get(key) + List_Talents_1[n].get(key)})
            else:
                Dict_Talents_1_item.update(
                    {key: Dict_Talents_1_item.get(key) or List_Talents_1[n].get(key)})
        n += 1

    Cha_Tal_2 = []
    Cha_Tal_2_s = Needs[name]["2技能初始"]
    while Cha_Tal_2_s <= Needs[name]["2技能目标"]:
        Cha_Tal_2.append(Cha_Tal_2_s)
        Cha_Tal_2_s += 1
    List_Talents_2 = []
    for lv in Cha_Tal_2:
        Csvlist[lv-1] = list(map(int, Csvlist[lv-1]))
        List_Talents = list_talents(name)
        Dict_Talents_2 = dict(zip(List_Talents, Csvlist[lv-1]))
        List_Talents_2.append(Dict_Talents_2)
    n = 0
    Dict_Talents_2_item = {}
    while n <= len(List_Talents_2)-1:
        for key in list(Dict_Talents_2_item | List_Talents_2[n]):
            if Dict_Talents_2_item.get(key) and List_Talents_2[n].get(key):
                Dict_Talents_2_item.update(
                    {key: Dict_Talents_2_item.get(key) + List_Talents_2[n].get(key)})
            else:
                Dict_Talents_2_item.update(
                    {key: Dict_Talents_2_item.get(key) or List_Talents_2[n].get(key)})
        n += 1
    Cha_Tal_3 = []
    Cha_Tal_3_s = Needs[name]["3技能初始"]
    while Cha_Tal_3_s <= Needs[name]["3技能目标"]:
        Cha_Tal_3.append(Cha_Tal_3_s)
        Cha_Tal_3_s += 1
    List_Talents_3 = []
    for lv in Cha_Tal_3:
        Csvlist[lv-1] = list(map(int, Csvlist[lv-1]))
        List_Talents = list_talents(name)
        Dict_Talents_3 = dict(zip(List_Talents, Csvlist[lv-1]))
        List_Talents_3.append(Dict_Talents_3)
    n = 0
    Dict_Talents_3_item = {}
    while n <= len(List_Talents_3)-1:
        for key in list(Dict_Talents_3_item | List_Talents_3[n]):
            if Dict_Talents_3_item.get(key) and List_Talents_3[n].get(key):
                Dict_Talents_3_item.update(
                    {key: Dict_Talents_3_item.get(key) + List_Talents_3[n].get(key)})
            else:
                Dict_Talents_3_item.update(
                    {key: Dict_Talents_3_item.get(key) or List_Talents_3[n].get(key)})
        n += 1
print()