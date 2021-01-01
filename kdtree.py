from sys import maxsize

class Node:
    def __init__(self, point):
        self.point = point
        self.left = None
        self.right = None
        self.upper_right = None
        self.lower_left = None

# Funkcja dokonująca zmiany punktów miejscami, punkty mniejsze od pivota po lewej
# stronie, większe po prawej.
def partition(arr,left,right, idx):
    pi=arr[right][idx]
    i=left-1

    for j in range(left,right):
        if arr[j][idx]<pi:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[right]=arr[right],arr[i+1]

    return i+1

# Funkcja ustawiająca elementy większego od k-tego (środkowego) elementy po jego
# prawej stronie, a mniejsze po lewej stronie. Działa w złożoności O(n).
def kthStatistics(arr,left,right,k, idx):
    i=partition(arr,left,right, idx)
    if i==k:
        return
    if i>k:
        kthStatistics(arr,left,i-1,k, idx)
    else:
        kthStatistics(arr,i+1,right,k, idx)

# idx wskazuje po którym elemencie chcemy porównywać
def median_idx(idx, points):
    n = len(points)
    kthStatistics(points,0, n-1, n//2, idx)
    return n//2

# najbardziej w górę i prawo wysunięty punkt -> do wizualizacji
def find_max(points):

    max_x = -maxsize
    max_y = -maxsize

    for x,y in points:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    return (max_x,max_y)

# najbardziej w górę i prawo wysunięty punkt -> do wizualizacji

def find_min(points):
    min_x = maxsize
    min_y = maxsize

    for x, y in points:
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y

    return (min_x, min_y)


class KDTree:
    def __init__(self,points, visualizer):
        self.root = self.construct(points, 0)
        self.visualizer = visualizer
        self.root.upper_right = find_max(points)
        self.root.lower_left = find_min(points)
        self.calculate_regions(self.root, 0)
        self.result =[]

    def construct(self, points, depth):
        n = len(points)

        if n<1:
            return None
        if n==1:
            return Node(points[0])

        idx = depth%2
        m = median_idx(idx,points)

        left = points[0:m]
        right = points[m+1:n]

        root = Node(points[m])
        left_child = self.construct(left, depth+1)
        right_child = self.construct(right, depth+1)
        root.right = right_child
        root.left = left_child

        return root

    def calculate_regions(self, root, depth):


        if root.right == None and root.left == None:
            root.lower_left = None
            root.upper_right = None
            return

        if self.visualizer:
            if depth%2==0:
                self.visualizer.add_line((root.point[0],root.lower_left[1]), (root.point[0], root.upper_right[1]))
            else:
                self.visualizer.add_line((root.lower_left[0], root.point[1]), (root.upper_right[0], root.point[1]))

        if root.right:
            if (depth%2==0):
                root.right.upper_right = root.upper_right
                root.right.lower_left = (root.point[0], root.lower_left[1])
            else:
                root.right.upper_right = root.upper_right
                root.right.lower_left = (root.lower_left[0], root.point[1])

            self.calculate_regions(root.right, depth+1)

        if root.left:
            if (depth%2==0):
                root.left.upper_right = (root.point[0], root.upper_right[1])
                root.left.lower_left = root.lower_left

            else:
                root.left.upper_right = (root.upper_right[0], root.point[1])
                root.left.lower_left = root.lower_left

            self.calculate_regions(root.left, depth+1)


    def report_subtree(self,  root):
        self.result.append(root.point)
        if self.visualizer:
            self.visualizer.add_point(root.point)

        if root.left:
            self.report_subtree(root.left)

        if root.right:
            self.report_subtree(root.right)

    def search(self, lower_left, upper_right):
        self.result = []
        if self.visualizer:
            self.visualizer.add_rectangle([lower_left, upper_right])

        self.search_kd_tree(self.root, lower_left, upper_right)
        return self.result

    def search_kd_tree(self, root, ll, ur):



        # aktualnie rozważany Node jest liściem
        if root.right == None and root.left == None:
            if point_inside(root.point, ll, ur):
                self.result.append(root.point)
                if self.visualizer:
                    self.visualizer.add_point(root.point)
            return

        if self.visualizer:
            self.visualizer.add_region(root.lower_left, root.upper_right)


        if point_inside(root.point, ll, ur):
            self.result.append(root.point)
            if self.visualizer:
                self.visualizer.add_point(root.point)

        if root.left:
            # rozważany prostokąt zawiera się w całości w obszarze obejmowanym przez root
            if region_inside(root.lower_left, root.upper_right, ll, ur):
                # wszystkie punkty z lewego poddrzewa znajdują sie w prostokącie
                self.report_subtree(root.left)

            # rozważany prostokąt przecina się z obszarem obejmowanym przez root
            elif region_intersects(root.lower_left, root.upper_right, ll, ur):
                self.search_kd_tree(root.left, ll, ur)

        if root.right:
            # rozważany prostokąt zawiera się w całości w obszarze obejmowanym przez root
            if region_inside(root.lower_left, root.upper_right, ll, ur):
                # wszystkie punkty z prawego poddrzewa znajdują sie w prostokącie
                self.report_subtree(root.right)

            # rozważany prostokąt przecina się z obszarem obejmowanym przez root
            elif region_intersects(root.lower_left, root.upper_right, ll, ur):
                self.search_kd_tree(root.right, ll, ur)


def point_inside(point, ll, ur):
    return point[0]>=ll[0] and point[0]<=ur[0] and point[1]>=ll[1] and point[1]<=ur[1]


def region_inside(region_ll, region_ur, ll, ur):
    return point_inside(region_ll, ll, ur) and point_inside(region_ur, ll, ur)

def region_intersects(region_ll, region_ur, ll, ur):
    return (point_inside(region_ll, ll, ur)
            or point_inside(region_ur, ll, ur)
            or point_inside(ll, region_ll, region_ur)
            or point_inside(ur, region_ll, region_ur)
            or point_inside((region_ll[0], region_ur[1]), ll, ur)
            or point_inside((ll[0], ur[1]), region_ll, region_ur))

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



