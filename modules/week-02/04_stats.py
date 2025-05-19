data= [15, 12, 19, 64, 23, 45, 78, 90, 100]

mean= sum(data)/len(data)
print("Mean:", mean)

#median
data.sort()
n = len(data)
if n % 2 == 1:
    median = data[n // 2]
else:
    median = (data[n // 2 - 1] + data[n // 2]) / 2
print("Median:", median)



products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Phone", "price": 600},
    {"name": "Headphones", "price": 150}
]

for item in products:
    item["price"] *= 0.9  

for item in products:
    print(f"{item['name']} now costs ${item['price']:.2f}")