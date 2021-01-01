from kdtree import KDTree
from quadtree import prepare_tree, find_points
from sys import maxsize

from random import random
import time

def random_points(lower_left, upper_right, n):

    points = [None]*n
    points_set = set()
    i =0
    while i < n:
        x = random()*upper_right[0]+lower_left[0]
        y = random()*upper_right[1]+lower_left[1]
        if (x,y) not in points_set:
            points_set.add((x,y))
            points[i] = (x,y)
            i+=1

    return points



def check_answers():
    print("##############################")
    print("##############################")
    print("    CORRECT ANSWER TESTS")
    print("##############################")
    print("##############################")
    print()
    print()
    print()

    ### TEST 1 ###
    points1 = [(20, 50), (30, 40), (35, 60), (50, 100), (60, 70), (10, 45), (10, 10), (45, 23), (7, 8), (1, 3),
               (18, 90), (80, 80)]
    region1 = [(40, 60), (90, 110)]
    answer1 = [(60, 70), (80, 80), (50, 100)]

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

    tree = prepare_tree(points1)
    result1 = find_points(tree, region1[1][1], region1[0][0], region1[0][1], region1[1][0])

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

    points2 = [(20, 50), (30, 40), (35, 60), (50, 100), (60, 70), (10, 45), (10, 10), (45, 23), (7, 8), (1, 3),
               (18, 90), (80, 80)]
    region2 = [(-maxsize, -maxsize), (maxsize, maxsize)]
    answer2 = [(20, 50), (30, 40), (35, 60), (50, 100), (60, 70), (10, 45), (10, 10), (45, 23), (7, 8), (1, 3),
               (18, 90), (80, 80)]

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

    tree = prepare_tree(points2)
    result2 = find_points(tree, region2[1][1], region2[0][0], region2[0][1], region2[1][0])

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

    points3 = [(20, 50), (30, 40), (35, 60), (50, 100), (60, 70), (10, 45), (10, 10), (45, 23), (7, 8), (1, 3),
               (18, 90), (80, 80)]
    region3 = [(1, 1), (1, 1)]
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

    tree = prepare_tree(points3)
    result3 = find_points(tree, region3[1][1], region3[0][0], region3[0][1], region3[1][0])

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

    points4 = [(20, 50), (30, 40), (35, 60), (50, 100), (60, 70), (10, 45), (10, 10), (45, 23), (7, 8), (1, 3),
               (18, 90), (80, 80)]
    region4 = [(10, 30), (40, 60)]
    answer4 = [(10, 45), (20, 50), (30, 40), (35, 60)]

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

    tree = prepare_tree(points4)
    result4 = find_points(tree, region4[1][1], region4[0][0], region4[0][1], region4[1][0])

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
    points5 = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)]
    region5 = [(1, 1), (3, 3)]
    answer5 = [(1, 1), (1, 2), (1, 3)]

    root5 = KDTree(points5, None)
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

    tree = prepare_tree(points5)
    result5 = find_points(tree, region5[1][1], region5[0][0], region5[0][1], region5[1][0])

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
    points6 = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (7, 7)]
    region6 = [(1, 1), (3, 3)]
    answer6 = [(1, 1), (1, 2), (1, 3)]

    root6 = KDTree(points6, None)
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

    tree = prepare_tree(points6)
    result6 = find_points(tree, region6[1][1], region6[0][0], region6[0][1], region6[1][0])

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
    points7 = [(1, 1), (1, 2), (1, 6), (3, 4), (4, 3), (4, 5), (4, 8), (5, 4), (6, 2), (6, 4), (7, 2), (7, 6), (9, 3),
               (10, 1), (10, 7)]
    region7 = [(2, 2), (7, 6)]
    answer7 = [(3, 4), (4, 3), (4, 5), (5, 4), (6, 2), (6, 4), (7, 2), (7, 6)]

    root7 = KDTree(points7, None)
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

    tree = prepare_tree(points7)
    result7 = find_points(tree, region7[1][1], region7[0][0], region7[0][1], region7[1][0])

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

def measure_time():

    ######################################
    ### PUNKTY W PRZEDZIALE 0-1000 #######
    print()
    print()
    print()
    print("##############################")
    print("##############################")
    print("        TIME TESTS")
    print("##############################")
    print("##############################")
    print()
    print()

    p1 = random_points((0, 0), (1000, 1000), 100)
    p2 = random_points((0, 0), (1000, 1000), 1000)
    p3 = random_points((0, 0), (1000, 1000), 10000)
    p4 = random_points((0, 0), (1000, 1000), 100000)
    p5 = random_points((0, 0), (1000, 1000), 1000000)

    region1 = [(0,0), (500,500)]
    region2 = [(0,0),(1000,1000)]
    region3 = [(0,0), (0,1000)]
    region4 = [(0, 0), (0, 10)]
    print()
    print("##############################")
    print("Points inside square 1000x1000")
    print("##############################")
    print()

    print("KDTree")
    start = time.time()
    root1 = KDTree(p1, None)
    end = time.time()
    print("Time for building tree for 100 points: ", end - start)

    start = time.time()
    root1.search(region1[0], region1[1])
    end = time.time()
    print("Finding 1/4 points: ", end - start)

    start = time.time()
    root1.search(region2[0], region2[1])
    end = time.time()
    print("Finding 1/1 points: ", end - start)

    start = time.time()
    root1.search(region3[0], region3[1])
    end = time.time()
    print("Finding 0/1 (line) points: ", end - start)

    start = time.time()
    root1.search(region4[0], region4[1])
    end = time.time()
    print("Finding 1/100 points: ", end - start)

    print()
    print("Quadtree")
    start = time.time()
    tree = prepare_tree(p1)
    end = time.time()
    print("Time for building tree for 100 points: ", end - start)

    start = time.time()
    find_points(tree, region1[1][1], region1[0][0], region1[0][1], region1[1][0])
    end = time.time()
    print("Finding 1/4 points: ", end - start)

    start = time.time()
    find_points(tree, region2[1][1], region2[0][0], region2[0][1], region2[1][0])
    end = time.time()
    print("Finding 1/1 points: ", end - start)

    start = time.time()
    find_points(tree, region3[1][1], region3[0][0], region3[0][1], region3[1][0])
    end = time.time()
    print("Finding 0/1 (line) points: ", end - start)

    start = time.time()
    find_points(tree, region4[1][1], region4[0][0], region4[0][1], region4[1][0])
    end = time.time()
    print("Finding 1/100 points: ", end - start)

    print()

    print("KDTree")
    start = time.time()
    root2 = KDTree(p2, None)
    end = time.time()
    print("Time for building tree for 1000 points: ", end - start)

    start = time.time()
    root2.search((0, 0), (500, 500))
    end = time.time()
    print("Finding 1/4 points: ", end - start)

    start = time.time()
    root2.search((0, 0), (1000, 1000))
    end = time.time()
    print("Finding 1/1 points: ", end - start)

    start = time.time()
    root2.search((0, 0), (0, 1000))
    end = time.time()
    print("Finding 0/1 (line) points: ", end - start)

    start = time.time()
    root2.search((0, 0), (0, 100))
    end = time.time()
    print("Finding 1/100 points: ", end - start)

    print()
    print("Quadtree")
    start = time.time()
    tree = prepare_tree(p2)
    end = time.time()
    print("Time for building tree for 1000 points: ", end - start)

    start = time.time()
    find_points(tree, region1[1][1], region1[0][0], region1[0][1], region1[1][0])
    end = time.time()
    print("Finding 1/4 points: ", end - start)

    start = time.time()
    find_points(tree, region2[1][1], region2[0][0], region2[0][1], region2[1][0])
    end = time.time()
    print("Finding 1/1 points: ", end - start)

    start = time.time()
    find_points(tree, region3[1][1], region3[0][0], region3[0][1], region3[1][0])
    end = time.time()
    print("Finding 0/1 (line) points: ", end - start)

    start = time.time()
    find_points(tree, region4[1][1], region4[0][0], region4[0][1], region4[1][0])
    end = time.time()
    print("Finding 1/100 points: ", end - start)

    print()

    print()

    print("KDTree")
    start = time.time()
    root3 = KDTree(p3, None)
    end = time.time()
    print("Time for building tree for 10000 points: ", end - start)

    start = time.time()
    root3.search((0, 0), (500, 500))
    end = time.time()
    print("Finding 1/4 points: ", end - start)

    start = time.time()
    root3.search((0, 0), (1000, 1000))
    end = time.time()
    print("Finding 1/1 points: ", end - start)

    start = time.time()
    root3.search((0, 0), (0, 1000))
    end = time.time()
    print("Finding 0/1 (line) points: ", end - start)

    start = time.time()
    root3.search((0, 0), (0, 100))
    end = time.time()
    print("Finding 1/100 points: ", end - start)

    print()
    print("Quadtree")
    start = time.time()
    tree = prepare_tree(p3)
    end = time.time()
    print("Time for building tree for 10000 points: ", end - start)

    start = time.time()
    find_points(tree, region1[1][1], region1[0][0], region1[0][1], region1[1][0])
    end = time.time()
    print("Finding 1/4 points: ", end - start)

    start = time.time()
    find_points(tree, region2[1][1], region2[0][0], region2[0][1], region2[1][0])
    end = time.time()
    print("Finding 1/1 points: ", end - start)

    start = time.time()
    find_points(tree, region3[1][1], region3[0][0], region3[0][1], region3[1][0])
    end = time.time()
    print("Finding 0/1 (line) points: ", end - start)

    start = time.time()
    find_points(tree, region4[1][1], region4[0][0], region4[0][1], region4[1][0])
    end = time.time()
    print("Finding 1/100 points: ", end - start)

    print()

    print()

    print("KDTree")
    start = time.time()
    root4 = KDTree(p4, None)
    end = time.time()
    print("Time for building tree for 100000 points: ", end - start)

    start = time.time()
    root4.search((0, 0), (500, 500))
    end = time.time()
    print("Finding 1/4 points: ", end - start)

    start = time.time()
    root4.search((0, 0), (1000, 1000))
    end = time.time()
    print("Finding 1/1 points: ", end - start)

    start = time.time()
    root4.search((0, 0), (0, 1000))
    end = time.time()
    print("Finding 0/1 (line) points: ", end - start)

    start = time.time()
    root4.search((0, 0), (0, 100))
    end = time.time()
    print("Finding 1/100 points: ", end - start)

    print()
    print("Quadtree")
    start = time.time()
    tree = prepare_tree(p4)
    end = time.time()
    print("Time for building tree for 100000 points: ", end - start)

    start = time.time()
    find_points(tree, region1[1][1], region1[0][0], region1[0][1], region1[1][0])
    end = time.time()
    print("Finding 1/4 points: ", end - start)

    start = time.time()
    find_points(tree, region2[1][1], region2[0][0], region2[0][1], region2[1][0])
    end = time.time()
    print("Finding 1/1 points: ", end - start)

    start = time.time()
    find_points(tree, region3[1][1], region3[0][0], region3[0][1], region3[1][0])
    end = time.time()
    print("Finding 0/1 (line) points: ", end - start)

    start = time.time()
    find_points(tree, region4[1][1], region4[0][0], region4[0][1], region4[1][0])
    end = time.time()
    print("Finding 1/100 points: ", end - start)

    print()

    print()

    print("KDTree")
    start = time.time()
    root5 = KDTree(p5, None)
    end = time.time()
    print("Time for building tree for 1000000 points: ", end - start)

    start = time.time()
    root5.search((0, 0), (500, 500))
    end = time.time()
    print("Finding 1/4 points: ", end - start)

    start = time.time()
    root5.search((0, 0), (1000, 1000))
    end = time.time()
    print("Finding 1/1 points: ", end - start)

    start = time.time()
    root5.search((0, 0), (0, 1000))
    end = time.time()
    print("Finding 0/1 (line) points: ", end - start)

    start = time.time()
    root5.search((0, 0), (0, 100))
    end = time.time()
    print("Finding 1/100 points: ", end - start)

    print()
    print("Quadtree")
    start = time.time()
    tree = prepare_tree(p5)
    end = time.time()
    print("Time for building tree for 1000000 points: ", end - start)

    start = time.time()
    find_points(tree, region1[1][1], region1[0][0], region1[0][1], region1[1][0])
    end = time.time()
    print("Finding 1/4 points: ", end - start)

    start = time.time()
    find_points(tree, region2[1][1], region2[0][0], region2[0][1], region2[1][0])
    end = time.time()
    print("Finding 1/1 points: ", end - start)

    start = time.time()
    find_points(tree, region3[1][1], region3[0][0], region3[0][1], region3[1][0])
    end = time.time()
    print("Finding 0/1 (line) points: ", end - start)

    start = time.time()
    find_points(tree, region4[1][1], region4[0][0], region4[0][1], region4[1][0])
    end = time.time()
    print("Finding 1/100 points: ", end - start)
    print()

    print()
    ### WSZYSTKIE PUNKTY NA JEDNEJ LINII ###
    p6 = random_points((0,0), (0,1000), 100)
    p7 = random_points((0,0), (0,1000), 1000) # dla większej ilości punktów przekraczam rozmiar stosu?
    region1 = [(0,0), (0,500)]
    region2 = [(0,0), (0,1000)]
    region3 = [(0, 0), (0, 100)]

    print()
    print("##############################")
    print("Points in line of length 1000")
    print("##############################")
    print()

    print("KDTree")
    start = time.time()
    root6 = KDTree(p6, None)
    end = time.time()
    print("Time for building tree for 100 points: ", end - start)

    start = time.time()
    root6.search((0, 0), (0, 500))
    end = time.time()
    print("Finding 1/2 points: ", end - start)

    start = time.time()
    root6.search((0, 0), (0, 1000))
    end = time.time()
    print("Finding 1/1 points: ", end - start)

    start = time.time()
    root6.search((0, 0), (0, 100))
    end = time.time()
    print("Finding 1/10 points: ", end - start)

    print()
    print("Quadtree")
    start = time.time()
    tree = prepare_tree(p6)
    end = time.time()
    print("Time for building tree for 100 points: ", end - start)

    start = time.time()
    find_points(tree, region1[1][1], region1[0][0], region1[0][1], region1[1][0])
    end = time.time()
    print("Finding 1/2 points: ", end - start)

    start = time.time()
    find_points(tree, region2[1][1], region2[0][0], region2[0][1], region2[1][0])
    end = time.time()
    print("Finding 1/1 points: ", end - start)

    start = time.time()
    find_points(tree, region3[1][1], region3[0][0], region3[0][1], region3[1][0])
    end = time.time()
    print("Finding 1/10 points: ", end - start)

    print()
    print()

    print("KDTree")
    start = time.time()
    root7 = KDTree(p7, None)
    end = time.time()
    print("Time for building tree for 1000 points: ", end - start)

    start = time.time()
    root7.search((0, 0), (0, 500))
    end = time.time()
    print("Finding 1/2 points: ", end - start)

    start = time.time()
    root7.search((0, 0), (0, 1000))
    end = time.time()
    print("Finding 1/1 points: ", end - start)

    start = time.time()
    root7.search((0, 0), (0, 100))
    end = time.time()
    print("Finding 1/10 points: ", end - start)

    print()
    print("Quadtree")
    start = time.time()
    tree = prepare_tree(p7)
    end = time.time()
    print("Time for building tree for 1000 points: ", end - start)

    start = time.time()
    find_points(tree, region1[1][1], region1[0][0], region1[0][1], region1[1][0])
    end = time.time()
    print("Finding 1/2 points: ", end - start)

    start = time.time()
    find_points(tree, region2[1][1], region2[0][0], region2[0][1], region2[1][0])
    end = time.time()
    print("Finding 1/1 points: ", end - start)

    start = time.time()
    find_points(tree, region3[1][1], region3[0][0], region3[0][1], region3[1][0])
    end = time.time()
    print("Finding 1/10 points: ", end - start)

    print()
    print()

    p10 = [(0.0, 0.0), (0.000000000001, 0.0), (1000000000000, 0.0)]
    region1 = [(0, 0), (0, 0)]

    print("Quadtree")
    start = time.time()
    tree = prepare_tree(p10)
    end = time.time()
    print("Time for building tree for p10: ", end - start)

    start = time.time()
    for i in range(100000):
        find_points(tree, region1[1][1], region1[0][0], region1[0][1], region1[1][0])
    end = time.time()
    print("Finding points: ", end - start)
    print()
    print("KDTree")
    start = time.time()
    root = KDTree(p10, None)
    end = time.time()
    print("Time for building tree for p10: ", end - start)

    start = time.time()
    for i in range(100000):
        root.search((0, 0), (0, 0))
    end = time.time()
    print("Finding points: ", end - start)





if __name__ == "__main__":
    check_answers()
    measure_time()




