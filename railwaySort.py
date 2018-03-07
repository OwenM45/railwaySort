inputFile = open("DATA30.txt","r")

data = inputFile.readlines()

biggestCar = 0
secondBiggestCar = 0

for line in data:
    cars = line.split(' ')
    if len(cars) <= 2:
        biggestCar = int(cars[0]) +1
    else:
        del cars[len(cars)-1]
        counter = 1
        moves = 0
        for car in cars:
            biggestCar -= 1
            for car in cars:
                secondBiggestCar = biggestCar-counter
                try:
                    if secondBiggestCar != 0:
                        if cars.index(str(secondBiggestCar)) > cars.index(str(biggestCar)):
                            tempCar = 0
                            tempCar = secondBiggestCar
                            moves += cars.index(str(secondBiggestCar))
                            del cars[cars.index((-1))]
                            cars.insert(0,str(tempCar))
                            counter += 1
                        else:
                            counter += 1
                except ValueError:
                    print('');
        print(moves)

        
inputFile.close()
    
        
    
