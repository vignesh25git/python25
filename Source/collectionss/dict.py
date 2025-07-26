d = { "Name":"Sachin",
      "Age":"42",
      "location":"Mumbai",
      "Profession":"Cricket"
}

for k,v in d.items():
    print(f'k {k} v {v}')

for k in d.keys():
    print(k)

for v in d.values():
    print(v)

print(f'Name is {d["Name"]}')

d.update({"location":"Bombay"})

print(d)

trips = {
    "UB001": {"trip_id": "UB001", "pickup": "Chennai",  "drop": "Airport",  "fare": 430},
    "UB002": {"trip_id": "UB002", "pickup": "Tambaram", "drop": "Central",  "fare": 320},
    "UB003": {"trip_id": "UB003", "pickup": "T-Nagar",  "drop": "Velachery", "fare": 210}
}

print(trips["UB001"]["pickup"])


