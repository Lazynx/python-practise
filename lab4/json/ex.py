import json


print(
    "Interface Status\n"
    "================================================================================\n"
    "DN                                                 Description           Speed    MTU\n"
    "-------------------------------------------------- --------------------  ------  ------"
)


with open("sample-data.json", "r") as file:
    json_data = json.load(file)

    for i_data in json_data['imdata']:
        print(f"{i_data['l1PhysIf']['attributes']['dn']}\t\t\t\t\t\t\t\t"
              f"{i_data['l1PhysIf']['attributes']['speed']}   {i_data['l1PhysIf']['attributes']['mtu']}")
