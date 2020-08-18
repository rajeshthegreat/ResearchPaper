from numpy import random as rm

from numpy import array


students = 75

courses = 4

a = []

preferences = [[0 for j in range(students)] for i in range(courses)]

for i in range(students):

    a = [1,2,3,4]
    
    rm.shuffle(a)
    
    while (len(a) > 0):

        j = rm.choice(courses)

        if (preferences[j][i] == 0):
            
            preferences[j][i] = rm.choice(a)

            a.remove(preferences[j][i])

print (preferences)

with open("Z:/EAproject/preferences.txt","w") as p:

    for i in range(courses):
        
        for j in range(students):

            p.write(str(preferences[i][j]) + ' ')

        p.write('\n')
