# continue

for letter in 'beteljesedes':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)




print("\n------------------------------------\n")



fruits = ["apple", "orange", "kiwi"] 
for fruit in fruits:
    if fruit == "orange":
        continue
    print(fruit)



print("\n------------------------------------\n")



teams = ["SAT", "SAAS", "MIT", "JITEM"]

iter_obj = iter(teams)

while True:
    try:
        team = next(iter_obj)
        print(team)
    except StopIteration:
        break