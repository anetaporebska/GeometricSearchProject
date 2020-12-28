from kdtree import KDTree
from sys import maxsize


### TEST 1 ###
points1 = [(20, 50), (30, 40), (35, 60), (50, 100), (60, 70), (10, 45),(10,10),(45,23),(7,8),(1,3),(18,90), (80,80)]
region1 = [(40,60), (90,110)]
answer1 = [(60,70), (80,80), (50,100)]

root1 = KDTree(points1, None)
result1 = root1.search(region1[0], region1[1])

print(" ########### TEST 1 ########### ")
if sorted(result1) == sorted(answer1):
    print("Correct!")
else:
    print("INCORRECT")
    print("Correct answer: ", end="")
    print(answer1)
    print("Your answer: ", end="")
    print(result1)

print()

### TEST 2 ###

points2 = [(20, 50), (30, 40), (35, 60), (50, 100), (60, 70), (10, 45),(10,10),(45,23),(7,8),(1,3),(18,90), (80,80)]
region2 = [(-maxsize,-maxsize), (maxsize,maxsize)]
answer2 = [(20, 50), (30, 40), (35, 60), (50, 100), (60, 70), (10, 45),(10,10),(45,23),(7,8),(1,3),(18,90), (80,80)]

root2 = KDTree(points2, None)
result2 = root2.search(region2[0], region2[1])

print(" ########### TEST 2 ########### ")
if sorted(result2) == sorted(answer2):
    print("Correct!")
else:
    print("INCORRECT")
    print("Correct answer: ", end="")
    print(answer2)
    print("Your answer: ", end="")
    print(result2)

print()

### TEST 3 ###

points3 = [(20, 50), (30, 40), (35, 60), (50, 100), (60, 70), (10, 45),(10,10),(45,23),(7,8),(1,3),(18,90), (80,80)]
region3 = [(1,1), (1,1)]
answer3 = []

root3 = KDTree(points3, None)
result3 = root3.search(region3[0], region3[1])

print(" ########### TEST 3 ########### ")
if sorted(result3) == sorted(answer3):
    print("Correct!")
else:
    print("INCORRECT")
    print("Correct answer: ", end="")
    print(answer3)
    print("Your answer: ", end="")
    print(result3)

print()


### TEST 4 ###

points4 = [(20, 50), (30, 40), (35, 60), (50, 100), (60, 70), (10, 45),(10,10),(45,23),(7,8),(1,3),(18,90), (80,80)]
region4 = [(10,30),(40,60)]
answer4 = [(10,45),(20,50),(30,40),(35,60)]

root4 = KDTree(points4, None)
result4 = root4.search(region4[0], region4[1])

print(" ########### TEST 4 ########### ")
if sorted(result4) == sorted(answer4):
    print("Correct!")
else:
    print("INCORRECT")
    print("Correct answer: ", end="")
    print(answer4)
    print("Your answer: ", end="")
    print(result4)

print()


### TEST 5 ###
points5 = [(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7)]
region5 = [(1,1),(3,3)]
answer5 = [(1,1), (1,2), (1,3)]

root5= KDTree(points5, None)
result5 = root5.search(region5[0], region5[1])

print(" ########### TEST 5 ########### ")
if sorted(result5) == sorted(answer5):
    print("Correct!")
else:
    print("INCORRECT")
    print("Correct answer: ", end="")
    print(answer5)
    print("Your answer: ", end="")
    print(result5)


print()


### TEST 6 ###
points6 = [(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7), (7,7)]
region6 = [(1,1),(3,3)]
answer6 = [(1,1), (1,2), (1,3)]

root6= KDTree(points6, None)
result6 = root6.search(region6[0], region6[1])

print(" ########### TEST 6 ########### ")
if sorted(result6) == sorted(answer6):
    print("Correct!")
else:
    print("INCORRECT")
    print("Correct answer: ", end="")
    print(answer6)
    print("Your answer: ", end="")
    print(result6)

print()


### TEST 7 ###
points7 = [(1,1),(1,2),(1,6),(3,4),(4,3),(4,5),(4,8),(5,4),(6,2),(6,4),(7,2),(7,6),(9,3),(10,1),(10,7)]
region7 = [(2,2),(7,6)]
answer7 = [(3,4),(4,3),(4,5),(5,4),(6,2),(6,4),(7,2),(7,6)]

root7= KDTree(points7, None)
result7 = root7.search(region7[0], region7[1])

print(" ########### TEST 7 ########### ")
if sorted(result7) == sorted(answer7):
    print("Correct!")
else:
    print("INCORRECT")
    print("Correct answer: ", end="")
    print(answer7)
    print("Your answer: ", end="")
    print(result7)



print()
print()

###################################################################################################################
###################################### TIME TESTS #################################################################

from random import randint
import time

def random_points(lower_left, upper_right, n):

    points = [None]*n

    for i in range(n):
        x = randint(lower_left[0], upper_right[0])
        y = randint(lower_left[1], upper_right[1])
        points[i] = (x,y)

    return points



def measure_time():

    ######################################
    ### PUNKTY W PRZEDZIALE 0-1000 #######
    # dla 1/4 punktów
    # dla wszystkich punktów
    # dla punktów na linii [(0,0), (0,1000)]

    p1 = random_points((0, 0), (1000, 1000), 100)
    p2 = random_points((0, 0), (1000, 1000), 1000)
    p3 = random_points((0, 0), (1000, 1000), 10000)
    p4 = random_points((0, 0), (1000, 1000), 100000)
    p5 = random_points((0, 0), (1000, 1000), 1000000)


    start = time.time()
    root1 = KDTree(p1, None)
    end = time.time()
    print("Time for building tree for p1: ", end - start)

    start = time.time()
    root1.search((0,0),(500,500))
    end = time.time()
    print("Finding points: ", end - start )

    start = time.time()
    root1.search((0, 0), (1000, 1000))
    end = time.time()
    print("Finding points: ", end - start)

    start = time.time()
    root1.search((0, 0), (0, 1000))
    end = time.time()
    print("Finding points: ", end - start)

    print()

    start = time.time()
    root2 = KDTree(p2, None)
    end = time.time()
    print("Time for building tree for p2: ", end - start)

    start = time.time()
    root2.search((0, 0), (500, 500))
    end = time.time()
    print("Finding points: ", end - start)

    start = time.time()
    root2.search((0, 0), (1000, 1000))
    end = time.time()
    print("Finding points: ", end - start)

    start = time.time()
    root2.search((0, 0), (0, 1000))
    end = time.time()
    print("Finding points: ", end - start)

    print()

    start = time.time()
    root3 = KDTree(p3, None)
    end = time.time()
    print("Time for building tree for p3: ", end - start)

    start = time.time()
    root3.search((0, 0), (500, 500))
    end = time.time()
    print("Finding points: ", end - start)

    start = time.time()
    root3.search((0, 0), (1000, 1000))
    end = time.time()
    print("Finding points: ", end - start)

    start = time.time()
    root3.search((0, 0), (0, 1000))
    end = time.time()
    print("Finding points: ", end - start)


    print()

    start = time.time()
    root4 = KDTree(p4, None)
    end = time.time()
    print("Time for building tree for p4: ", end - start)

    start = time.time()
    root4.search((0, 0), (500, 500))
    end = time.time()
    print("Finding points: ", end - start)

    start = time.time()
    root4.search((0, 0), (1000, 1000))
    end = time.time()
    print("Finding points: ", end - start)

    start = time.time()
    root4.search((0, 0), (0,1000))
    end = time.time()
    print("Finding points: ", end - start)

    print()

    start = time.time()
    root5 = KDTree(p5, None)
    end = time.time()
    print("Time for building tree for p5: ", end - start)

    start = time.time()
    root5.search((0, 0), (500, 500))
    end = time.time()
    print("Finding points: ", end - start)

    start = time.time()
    root5.search((0, 0), (1000, 1000))
    end = time.time()
    print("Finding points: ", end - start)

    start = time.time()
    root5.search((0, 0), (0, 1000))
    end = time.time()
    print("Finding points: ", end - start)

    print()

    ### WSZYSTKIE PUNKTY NA JEDNEJ LINII ###
    p6 = random_points((0,0), (0,1000), 100)
    p7 = random_points((0,0), (0,1000), 1000) # dla większej ilości punktów przekraczam rozmiar stosu?

    start = time.time()
    root6 = KDTree(p6, None)
    end = time.time()
    print("Time for building tree for p6: ", end - start)

    start = time.time()
    root6.search((0, 0), (0, 500))
    end = time.time()
    print("Finding points: ", end - start)

    start = time.time()
    root6.search((0, 0), (0, 1000))
    end = time.time()
    print("Finding points: ", end - start)

    print()

    start = time.time()
    root7 = KDTree(p7, None)
    end = time.time()
    print("Time for building tree for p7: ", end - start)

    start = time.time()
    root7.search((0, 0), (0, 500))
    end = time.time()
    print("Finding points: ", end - start)

    start = time.time()
    root7.search((0, 0), (0, 1000))
    end = time.time()
    print("Finding points: ", end - start)




if __name__ == "__main__":
    measure_time()




