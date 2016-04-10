import readline

foodAlreadyRequested = []
foodAvailable = ["banana", "cookies", "pizza", "macarrones"]

def requestFood(food):
    if food in foodAlreadyRequested:
        print("I think you've already ordered "+food+".")
    elif food in foodAvailable:
        print("You ordered "+food+".")
        foodAlreadyRequested.append(food)
    else:
        print("Sorry, we don't have "+food+" :/")

doyouwanttocontinue = True

while doyouwanttocontinue == True:
    foodRequested = input("What do you want? ").lower()
    requestFood(foodRequested)
    if input("Do you want anything else? ").lower() in ["no", "n", ""]:
        print("Sweet, see ya!")
        doyouwanttocontinue = False