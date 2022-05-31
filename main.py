
locationList = ["air1","air2", "air3","air4","air5","air6"]

location = input("Choose your starting location. You can choose "+locationList[0]+", "+locationList[1]+", "+locationList[2]+", "+locationList[3]+", "+locationList[4]+", or "+locationList[5]+".")

if location in locationList:
    pass
else:
    print("NOT AN OPTION")
