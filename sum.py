import json

filepath = "satellite_time.json"
file = open(filepath)
data = json.load(file)

total_sum = sum(data.values())
Mbps = total_sum * 50
print("Total sum:", Mbps, "Mb/doba")