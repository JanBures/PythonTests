import json


data = {
    "Jmeno": "Pavel",
    "Auto":[{"BMW":1.5},{"BMW":3.7}],
    "Deti":True,
    "Jmena deti":["Matouš","Pavel","Lucie"],
    "Zenaty":True,
    "Manzelka":"Marie"
}

print(data)


print(json.dumps(data, indent=4))