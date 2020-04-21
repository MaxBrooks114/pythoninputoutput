import shelve

fruit = shelve.open('shelftest')
fruit['orange'] = "a sweet fruit"
fruit['kiwi'] = "hairy"
fruit['strawberry'] = "little seeds"

print(fruit["kiwi"])
print(fruit["orange"])

fruit.close()