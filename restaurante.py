import readline

foodAvailable = ["Banana", "Cookies", "Pizza", "Macarrones"]

def requestFood(food):
    if food in foodAvailable:
        print("You ordered "+food+".")
    else:
        print("Sorry, we don't have "+food+" :/")

doyouwanttocontinue = True

while doyouwanttocontinue == True:
    foodRequested = input("What do you want? ")
    requestFood(foodRequested)
    if input("Do you want anything else? ") in ["No", "no", "N", "n"]:
        doyouwanttocontinue = False