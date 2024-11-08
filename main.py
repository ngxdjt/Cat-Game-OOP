from cat import Cat

print("Welcome to my cat game!")

name = input("Enter your cat's name: ")
colour = input("Enter your cat's colour: ")

cat = Cat(name,colour)

while cat.checkDeath():
    option = input("\nWhat would you like to do? \n1. Play with your cat \n2. Train your cat \n3. Feed your cat \n4. Put your cat to sleep \n5. Show stats\n")
    print("\033[A\033[K")

    if option == "1":
        cat.play()
    elif option == "2":
        cat.train()
    elif option == "3":
        cat.feed()
    elif option == "4":
        cat.sleep()
    elif option == "5":
        cat.stats

    
