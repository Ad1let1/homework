import json

with open("sample-data.json", "r") as file:
    data = json.load(file)
print("Interface Status")
print("================================================================================")
print("DN                                         Description        Speed    MTU")
print("------------------------------------------ -----------        -----    ---")

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    descr = attributes.get("descr", "N/A")
    speed = attributes["speed"]
    dn = attributes["dn"]
    mtu = attributes["mtu"]

    print(f"{dn:<45} {descr:<15} {speed:<8} {mtu:<6}")