from sys import maxsize

# TODO wizualizacja
# TODO komentarze
# TODO posprzątać kod
# TODO dodać bardziej zaawansowane testy
# TODO co z punktami, które leżą na dzielących liniach, gdzie są przyporządkowywane
# TODO dokumentacja

class Node:
    def __init__(self, point):
        self.point = point
        self.left = None
        self.right = None
        self.upper_right = None
        self.lower_left = None


def partition(arr,left,right, idx):
    pi=arr[right][idx]
    i=left-1

    for j in range(left,right):
        if arr[j][idx]<pi:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[right]=arr[right],arr[i+1]

    return i+1

def kthStatistics(arr,left,right,k, idx):
    i=partition(arr,left,right, idx)
    if i==k:
        return arr[i]
    if i>k:
        kthStatistics(arr,left,i-1,k, idx)
    else:
        kthStatistics(arr,i+1,right,k, idx)

# idx wskazuje po którym elemencie chcemy porównywać
def median_idx(idx, points):
    n = len(points)
    kthStatistics(points,0, n-1, n//2, idx)
    return n//2

class KDTree:
    def __init__(self,points):
        self.root = self.construct(points, 0, None)
        self.root.upper_right = (maxsize, maxsize)
        self.root.lower_left = (-maxsize, -maxsize)
        self.calculate_regions(self.root, 0)
        self.result =[]

    def construct(self, points, depth, parent):
        # posortować po x i po y
        #
        n = len(points)
        if n<1:
            return None

        if n==1:
            return Node(points[0])

        if depth%2 == 0:

            m = median_idx(0,points)
            left = points[0:m]
            right = points[m+1:n]

        else:
            m = median_idx(1,points)
            left = points[0:m]
            right = points[m+1:n]

        root = Node(points[m])
        left_child = self.construct(left, depth+1, root)
        right_child = self.construct(right, depth+1, root)

        root.right = right_child
        root.left = left_child

        return root

    def calculate_regions(self, root, depth):

        if root.right == None and root.left == None:
            root.lower_left = None
            root.upper_right = None


        if root.right:

            if (depth%2==0):
                root.right.upper_right = root.upper_right
                root.right.lower_left = (root.point[0], root.lower_left[1])

            else:
                root.right.upper_right = root.upper_right
                root.right.lower_left = (root.lower_left[0], root.point[1])

            self.calculate_regions(root.right, depth+1)

        if root.left:

            # sortowane po x
            if (depth%2==0):
                root.left.upper_right = (root.point[0], root.upper_right[1])
                root.left.lower_left = root.lower_left

            else:
                root.left.upper_right = (root.upper_right[0], root.point[1])
                root.left.lower_left = root.lower_left

            self.calculate_regions(root.left, depth+1)

    def report_subtree(self,  root):
        self.result.append(root.point)
        if root.left:
            self.report_subtree(root.left)

        if root.right:
            self.report_subtree(root.right)

    def search(self, lower_left, upper_right):
        self.result = []
        self.search_kd_tree(self.root, lower_left, upper_right)
        return self.result

    def search_kd_tree(self, root, ll, ur):

        # v is a leaf
        if root.right == None and root.left == None:
            if point_inside(root.point, ll, ur):
                self.result.append(root.point)
                return

        if point_inside(root.point, ll, ur):
            self.result.append(root.point)

        # region lc(v) is fully contained in R
        if root.left:
            if region_inside(root.lower_left, root.upper_right, ll, ur):
                # report subtree lc(v)
                self.report_subtree(root.left)

            # region lc(v) intersects R
            elif region_intersects(root.lower_left, root.upper_right, ll, ur):
                self.search_kd_tree(root.left, ll, ur)

        if root.right:
            if region_inside(root.lower_left, root.upper_right, ll, ur):
                self.report_subtree(root.right)

            elif region_intersects(root.lower_left, root.upper_right, ll, ur):
                self.search_kd_tree(root.right, ll, ur)


def point_inside(point, ll, ur):
    return point[0]>=ll[0] and point[0]<=ur[0] and point[1]>=ll[1] and point[1]<=ur[1]


def region_inside(region_ll, region_ur, ll, ur):
    return point_inside(region_ll, ll, ur) and point_inside(region_ur, ll, ur)

def region_intersects(region_ll, region_ur, ll, ur):
    return point_inside(region_ll, ll, ur) or point_inside(region_ur, ll, ur) or point_inside(ll, region_ll, region_ur) or point_inside(ur, region_ll, region_ur)

def traverse(root, depth):
    if not root:
        return

    if root.left:
        traverse(root.left, depth+1)

    if root.right:
        traverse(root.right, depth+1)

    print("depth: ", depth, " ",  root.point, end ="")
    if root.left: print(" left: ", root.left.point, end="")
    if root.right: print( " right: ", root.right.point, end="")
    if root.lower_left: print(" lower left : ", root.lower_left, end="")
    if root.upper_right: print(" upper right: ", root.upper_right, end="")

    print("")






if __name__ == "__main__":
    points1 = [(20,50),(30,40),(30,60)]
    root1 = KDTree(points1)
    traverse(root1.root,1)

    print("drugi")
    points2 = [(20, 50), (30, 40), (30, 60), (50,100),(60,70),(30,65),(10,45)]
    root2 = KDTree(points2)
    traverse(root2.root,1)


    print("trzeci")
    points3 = [(20, 50), (30, 40), (30, 60), (50, 100), (60, 70), (30, 60), (10, 45), (100,100),(30,50),(40,40),(20,20),(20,10),(45,23),(7,8),(1,3),(18,90)]
    root3 = KDTree(points3)
    traverse(root3.root,1)


    print("czwarty") # wszystkie punkty różne x i y
    points4 = [(20, 50), (30, 40), (35, 60), (50, 100), (60, 70), (10, 45),(10,10),(45,23),(7,8),(1,3),(18,90), (80,80)]
    root4 = KDTree(points4)
    traverse(root4.root, 1)

    result = root4.search((40,60), (90,110))
    print("RESULT: ")
    print(result)



