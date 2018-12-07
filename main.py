import pandas as pd
from collections import OrderedDict
from building import Building
from pprint import pprint
import time

def get_buildings_from_file():
    d = pd.read_excel("building_data.xlsx", sheet_name="Sheet1", names=[
        "date_added",
        "occupancy",
        "lease_signed",
        "building",
        "building_class",
        "city",
        "deal_size",
        "tenant",
        "new_renewal_expansion",
        "term",
        "base_rent",
        "rent_structure",
        "esc",
        "t_i",
        "rent_abatement",
        "tenant_broker",
        "ll_broker",
        "t_o",
        "comments"])
    od = d.where((pd.notnull(d)), None).to_dict(orient="index", into=OrderedDict)
    buildings = []
    for i in range(len(od)):
        building = Building(**od[i])
        buildings.append(building)
    print(buildings[0].to_json)
    return buildings

def user_ui():
    """
    user_ui asks for query keys
    """
    print("Select one of the following:")
    print("Tip: you can separate with commas.")
    print("Get all buildings info -> (ALL)")
    print("Date Added -> (da)")
    print("Occupancy -> (oc)")
    print("Lease Signed -> (ls)")
    print("Building Name-> (bu)")
    print("Building Class -> (bc)")
    print("City -> (ci)")
    print("Deal Size -> (ds)")
    print("Tenant -> (te)")
    print("New / Renewal / Expansion -> (nr)")
    print("Term -> (tm)")
    print("Base Rent -> (br)")
    print("Rent Structure -> (rs)")
    print("Esc -> (es)")
    print("T/I -> (ti)")
    print("Rent Abatement -> (ra)")
    print("Tenant Broker -> (tb)")
    print("LL Broker -> (lb)")
    print("T/O -> (to)")
    print("Comments -> (co)")
    print("Would you a list of only these speifications (l),")
    want_all_data = False
    all_or_not = input("or the building (b) that meets these: ")
    if all_or_not.lower() == "l":
        want_all_data = False
    elif all_or_not.lower() == "b":
        want_all_data = True
    else:
        print("Wrong keyword. Use 'l' or 'b'")
        time.sleep(2)
        user_ui()

    inp = input("Search: ")
    if inp.upper() == "ALL".upper():
        return get_all_buildings_data()
    queries = [x.strip() for x in inp.split(",")]
    validate_queries(queries)
    filtered_dicts = get_key_values(queries)
    buildings = get_buildings_from_file()
    temp_arr = []
    for b in buildings:
        for d in filtered_dicts:
            if want_all_data:
                b_d = b.to_json
                for k, v in d.items():
                    if b_d[k] == v:
                        print(b_d)
                        print("\n")
                # else:
                #     print("We couldn't find your building. Would you like to try again:")
                #     if bool(input("(True) or (False): ").capitalized()):
                #         user_ui()
                    # else:
                    #     return
            else:
                print("OK")

def get_all_buildings_data():
    buildings = get_buildings_from_file()
    print("Printing Buildings...")
    time.sleep(2)
    for b in buildings:
        pprint(vars(b))
    return

def validate_queries(queries):
    """
    Validates query inputs
    """
    valid_queries = ["da","oc","ls","bu","bc","ci","ds","te","nr","tm","br","rs","es","ti","ra","tb","lb","to","co",]
    assigned_queries = []
    for q in set(queries):
        if q not in valid_queries:
            print("\n\n%s is not in the options provided\n\n" % q)
            time.sleep(4)
            user_ui()
        elif len(q) != 2:
            print("%s is not two letters" % q)
            time.sleep(4)
            user_ui()
        else:
            assigned_queries.append(assign_query(q))

def assign_query(query):
    """
    Assigns each input provided to a Building object's property
    """
    if query == "da":
        return "date_added"
    elif query == "oc":
        return "occupancy"
    elif query == "ls":
        return "lease_signed"
    elif query == "bu":
        return "building"
    elif query == "bc":
        return "building_class"
    elif query == "ci":
        return "city"
    elif query == "ds":
        return "deal_size"
    elif query == "te":
        return "tenant"
    elif query == "nr":
        return "new_renewal_expansion"
    elif query == "tm":
        return "term"
    elif query == "br":
        return "base_rent"
    elif query == "rs":
        return "rent_structure"
    elif query == "es":
        return "esc"
    elif query == "ti":
        return "t_i"
    elif query == "ra":
        return "rent_abatement"
    elif query == "tb":
        return "tenant_broker"
    elif query == "lb":
        return "ll_broker"
    elif query == "to":
        return "t_o"
    elif query == "co":
        return "comments"

    print("\nSuccess!!\n")

def get_readable_value(query):
    """
    Assigns each input provided to a Building object's property
    """
    if query == "da":
        return "Date Added"
    elif query == "oc":
        return "Occupancy"
    elif query == "ls":
        return "Lease Signed"
    elif query == "bu":
        return "Building"
    elif query == "bc":
        return "Building Class"
    elif query == "ci":
        return "City"
    elif query == "ds":
        return "Deal Size"
    elif query == "te":
        return "Tenant"
    elif query == "nr":
        return "New / renewal / expansion"
    elif query == "tm":
        return "Term"
    elif query == "br":
        return "Base Rent"
    elif query == "rs":
        return "Rent Structure"
    elif query == "es":
        return "Esc"
    elif query == "ti":
        return "T/I"
    elif query == "ra":
        return "Rent Abatement"
    elif query == "tb":
        return "Tenant Broker"
    elif query == "lb":
        return "LL Broker"
    elif query == "to":
        return "T/O"
    elif query == "co":
        return "Comments"

def get_key_values(queries):
    filtered_dicts = []
    for query in queries:
        qs = get_readable_value(query)
        inp = input("What's your value for %s? " % qs)
        if inp == "":
            print("Cannot leave object blank")
            user_ui()
        else:
            k = assign_query(query)
            fd = {k: inp}
            filtered_dicts.append(fd)
    return filtered_dicts

def main():
    get_buildings_from_file()
    user_ui()

main()
