import json

with open(r"C:\Users\Askar\Documents\TI\html\sample-data.json") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
print("-" * 80)

for item in data["imdata"]:
    dn = item["l1PhysIf"]["attributes"]["dn"]
    desc = item["l1PhysIf"]["attributes"].get("descr", "")  
    speed = item["l1PhysIf"]["attributes"].get("speed", "inherit")
    mtu = item["l1PhysIf"]["attributes"]["mtu"]

    print(f"{dn:<50} {desc:<20} {speed:<7} {mtu:<6}")





Interface Status
================================================================================
DN                                                 Description          Speed   MTU
--------------------------------------------------------------------------------
topology/pod-1/node-201/sys/phys-[eth1/33]                              inherit 9150
topology/pod-1/node-201/sys/phys-[eth1/34]                              inherit 9150
topology/pod-1/node-201/sys/phys-[eth1/35]                              inherit 9150
topology/pod-1/node-201/sys/phys-[eth1/36]                              inherit 9150
topology/pod-1/node-201/sys/phys-[eth1/1]                               inherit 9150
topology/pod-1/node-201/sys/phys-[eth1/2]                               inherit 9150
topology/pod-1/node-201/sys/phys-[eth1/3]                               inherit 9150
topology/pod-1/node-201/sys/phys-[eth1/4]                               inherit 9150
topology/pod-1/node-201/sys/phys-[eth1/5]                               inherit 9150
topology/pod-1/node-201/sys/phys-[eth1/6]                               inherit 9150
topology/pod-1/node-201/sys/phys-[eth1/7]                               inherit 9150
topology/pod-1/node-201/sys/phys-[eth1/8]                               inherit 9150
topology/pod-1/node-201/sys/phys-[eth1/9]                               inherit 9150
topology/pod-1/node-201/sys/phys-[eth1/10]                              inherit 9150
topology/pod-1/node-201/sys/phys-[eth1/11]                              inherit 9150
topology/pod-1/node-201/sys/phys-[eth1/12]                              inherit 9150
topology/pod-1/node-201/sys/phys-[eth1/13]                              inherit 9150
topology/pod-1/node-201/sys/phys-[eth1/14]                              inherit 9150
