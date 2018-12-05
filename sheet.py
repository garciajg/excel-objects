import pandas as pd
from collections import OrderedDict
from building import Building

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
