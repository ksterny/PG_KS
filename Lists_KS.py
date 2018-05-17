name = "Katherine"

subjects = ["English","Math","Spanish","History","Science","Art"]

print("Hello " + name)

for i in subjects:
    print("One of my classes is " + i)


dogs = ["English Springer Spaniel","Blood Hound","Collie","Australian Shepherd"]

for i in dogs:
    if i == "Blood Hound":
        print(i + " is a type of hunting dog.")
    elif i == "Collie":
        print(i + " is a fluffy dog")
    else:
        print("One of my favorite dog breeds is " + i)


dogs = []

while True:
    print("What dogs do you like? Type 'end' to quit.")
    answer = input()

    if answer == "end":
        break
    else:
        movies.append(answer)

for i in dogs:
    print("One of your favorites is" + i)
