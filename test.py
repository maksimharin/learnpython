a = {"city":"Moscow", "temperature":"13", "wind":"North" }
b = {"city":"New York", "temperature":"12", "wind":"West" }
c = {"city":"", "temperature":"", "wind":"" }
people = {"Tom":a, "Mary":b, "Bob":c}
name = input("введите имя: ")
print(people[name])