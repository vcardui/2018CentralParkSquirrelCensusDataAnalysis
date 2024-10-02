import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data["Primary Fur Color"])

gray = 0
red = 0
black = 0
for item in data["Primary Fur Color"]:
    if item == 'Gray':
        gray += 1
    elif item == 'Cinnamon':
        red += 1
    elif item == 'Black':
        black += 1

print(f"gray = {gray}")
print(f"red = {red}")
print(f"black = {black}")

furColor_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray, red, black]
}

furColor_data = pandas.DataFrame(furColor_dict)
print(furColor_data)
furColor_data.to_csv("furColor_data.csv")
