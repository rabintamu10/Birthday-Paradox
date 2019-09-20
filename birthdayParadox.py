
import random
birthDates = [360+1]
noOfPeople = 5
for i in range(0,birthDates.__len__(),1):
    birthDates[i] = i+1
iteration = 0
while noOfPeople<=100:
    print("Number of people:",noOfPeople)
    newbirth_day = [noOfPeople]
    count = 0
    iteration = 100000
    while iteration != 0:
        count = 0
        for i in range(0,newbirth_day.__len__(),1):
            day = random.randint(1,10)
            newbirth_day[i] = birthDates[day]
        for i in range(0,newbirth_day.__len__(),1):
            bday = newbirth_day[i]
            for j in range(0,newbirth_day.__len__(),1):
                if bday == newbirth_day[j]:
                    count += 1
                    break
        iteration -= 1
    print("Probability: " ,count ,"/",100000)
    print()
    noOfPeople += 5

