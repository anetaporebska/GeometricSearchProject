# super profesjonalny plik z testami

from kdtree import KDTree
from sys import maxsize

# TODO dodać pomiar czasu


### TEST 1 ###
points1 = [(20, 50), (30, 40), (35, 60), (50, 100), (60, 70), (10, 45),(10,10),(45,23),(7,8),(1,3),(18,90), (80,80)]
region1 = [(40,60), (90,110)]
answer1 = [(60,70), (80,80), (50,100)]

root1 = KDTree(points1)
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

root2 = KDTree(points2)
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

root3 = KDTree(points3)
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

root4 = KDTree(points4)
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

