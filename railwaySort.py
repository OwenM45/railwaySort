#open input file
inputFile = open("DATA31.txt","r")

#read the file into an array by lines
data = inputFile.readlines()

#set the variables for second biggest and biggest car
biggestCar = 0
secondBiggestCar = 0

#set the variable for the amount of moves
moves = 0
for line in data:
    #splits the line into an array of cars
    cars = line.split()

    #checks if the line is telling the num of cars or the list of cars
    if len(cars) == 1:
        #set the size of the biggest car
        biggestCar = int(cars[0])
        #set the amount of moves back to 0
        moves = 0
    else:
        #loop through the cars in the train
        for car in cars:
            try:
                #check if the next biggest car is ahead of the biggest
                if cars.index(str(biggestCar)) < cars.index(str(biggestCar-1)):
                    #move the next biggest car to the back of the train 
                    tempCar = 0
                    tempCar = biggestCar-1
                    moves += cars.index(str(biggestCar-1))
                    del cars[cars.index(str(biggestCar-1))]
                    cars.insert(0,str(tempCar))
                #sets the biggest car to the next biggest car
                biggestCar -=1
            except ValueError:
                #prints how many moves it took
                print(moves)
#closes the file
inputFile.close()
    
        
    
