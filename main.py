timeSpend = {
    "html+css": 8,
    "html+css+js": 12,
    "setup_wordpress": 8,
    "setup_wordpress_plugin": 4,
    "crud_laravel": 6,
    "seo_by_page": 1,
    "tests": 3
}

itemDoing = {}

priceByItems = {}

timeActive = 8
projectPrice = 0
projectTime = 0

for item in timeSpend:
    itemDoing[item] = float(input("Quantos " + str(item) + " serão feitos: "))
    priceByItems[item] = itemDoing[item] * timeSpend[item]

hourPrice = float(input("Valor hora: "))

for item in priceByItems:
    projectTime = projectTime + priceByItems[item]
    priceByItems[item] = priceByItems[item] * hourPrice
    projectPrice = projectPrice + priceByItems[item]

print("\nValor do projeto: R$ " + str(projectPrice))
print("Prazo do projeto: " + str(projectTime) + " horas")
print("Dias úteis de projeto: " + str(projectTime / timeActive))
