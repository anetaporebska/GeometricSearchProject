import math

northeast = top = x = 0
northwest = left = y = 1
southwest = bottom = 2
southeast = right = 3


#klasa przechowujaca wezly drzewa, kolejne atrybuty przechowuja kolejno:
#tablice z granicami obejmowanego obszaru
#tablice z dziecmi wezla (inny wezel/punkt/None)
#informacje, czy wezel jest dzieckiem, przechowujacym punkt
class Node:
    def __init__(self, top_boundary, left_boundary, bottom_boundary, right_boundary):
        self.boundaries = (top_boundary, left_boundary, bottom_boundary, right_boundary)
        self.children = [None, None, None, None]
        self.is_child_leaf = [False, False, False, False]


#klasa przechowujaca korzen drzewa, kolejne atrybuty przechowuja kolejno:
#informacje, czy drzewo nie posiada punktow
#informacje, czy drzewo zawiera tylko jeden punkt
#zapisany punkt, jezeli drzewo zawiera tylko jeden punkt
#pierwszy wezel drzewa, jezeli zawiera ono wiecej niz jeden punkt
class Root:
    def __init__(self, no_points, is_leaf, leaf_point, node):
        self.no_points = no_points
        self.is_leaf = is_leaf
        self.leaf_point = leaf_point
        self.node = node


#funkcja, usuwajaca ze zbioru powtarzajace sie punkty
def del_repeated(points):
    points.sort(key = lambda point: point[x])
    for point_index in range(len(points) - 1, 0, -1):
        if points[point_index][x] == points[point_index - 1][x] and points[point_index][y] == points[point_index - 1][y]:
            del points[point_index]


#funkcja odnajdujaca najdalej wysuniete wspolrzedne zbioru punktow (kolejno: lewa, prawa, dolna, gorna)
def found_boundaries(points):
    min_horizontal = math.inf
    max_horizontal = -math.inf
    min_vertical = math.inf
    max_vertical = -math.inf

    for point in points:
        min_horizontal = min(min_horizontal, point[x])
        max_horizontal = max(max_horizontal, point[x])
        min_vertical = min(min_vertical, point[y])
        max_vertical = max(max_vertical, point[y])

    return min_horizontal, max_horizontal, min_vertical, max_vertical


#funkcja tworzaca kolejne dzieci wezla, moga to byc nowe wezly, liscie zawierajace punkt lub wartosci None
def prepare_next_nodes(parent, points):
    split_vertical = (parent.boundaries[top] + parent.boundaries[bottom]) / 2
    split_horizontal = (parent.boundaries[left] + parent.boundaries[right]) / 2

    children_points = [[], [], [], []]

    for point in points:
        if point[x] <= split_horizontal:
            if point[y] <= split_vertical:
                children_points[southwest].append(point)
            else:
                children_points[northwest].append(point)
        else:
            if point[y] <= split_vertical:
                children_points[southeast].append(point)
            else:
                children_points[northeast].append(point)

    for child_index in range(4):
        if len(children_points[child_index]) == 1:
            parent.children[child_index] = children_points[child_index][0]
            parent.is_child_leaf[child_index] = True

        elif len(children_points[child_index]) > 1:
            if child_index == northeast:
                new_children = Node(parent.boundaries[top], split_horizontal, split_vertical, parent.boundaries[right])
            if child_index == northwest:
                new_children = Node(parent.boundaries[top], parent.boundaries[left], split_vertical, split_horizontal)
            if child_index == southwest:
                new_children = Node(split_vertical, parent.boundaries[left], parent.boundaries[bottom], split_horizontal)
            if child_index == southeast:
                new_children = Node(split_vertical, split_horizontal, parent.boundaries[bottom], parent.boundaries[right])

            parent.children[child_index] = new_children
            prepare_next_nodes(new_children, children_points[child_index])


#funkcja tworzaca korzen drzewa
def create_root(points):
    if len(points) == 0:
        return Root(True, False, None, None)
    if len(points) == 1:
        return Root(False, True, points[0], None)

    left_boundary, right_boundary, bottom_boundary, top_boundary = found_boundaries(points)
    return Root(False, False, None, Node(top_boundary, left_boundary, bottom_boundary, right_boundary))


#funkcja przygotowuje cale drzewo, jezeli wystepuja powtarzajace sie punkty, nalezy podac jako drugi parametr True
def prepare_tree(points, delete = False):
    if delete:
        del_repeated(points)
    root = create_root(points)

    if root.no_points == False and root.is_leaf == False:
        prepare_next_nodes(root.node, points)

    return root


#funkcja sprawdzajaca, czy obszar obejmowany przez wezel w jakimkolwiek miejscu pokrywa sie z granicami sprawdzanego obszaru
def field_inside(field, top_boundary, left_boundary, bottom_boundary, right_boundary):
    if field.boundaries[top] < bottom_boundary:
        return False
    if field.boundaries[bottom] > top_boundary:
        return False
    if field.boundaries[left] > right_boundary:
        return False
    if field.boundaries[right] < left_boundary:
        return False

    return True


#funkcja znajdujaca w przekazanym poddrzewie punkty, lezace wewnatrz wskazanego obszaru
def find_in_nodes(parent, top_boundary, left_boundary, bottom_boundary, right_boundary):
    points_inside = []
    for child_index in range(4):
        if parent.is_child_leaf[child_index]:
            child = parent.children[child_index]
            if bottom_boundary <= child[y] <= top_boundary and left_boundary <= child[x] <= right_boundary:
                points_inside.append(child)

        elif parent.children[child_index] != None:
            child = parent.children[child_index]
            if field_inside(child, top_boundary, left_boundary, bottom_boundary, right_boundary):
                points_inside += find_in_nodes(child, top_boundary, left_boundary, bottom_boundary, right_boundary)

    return points_inside


#funkcja znajdujaca w przekazanym drzewie punkty, lezace wewnatrz wskazanego obszaru
def find_points(root, top_boundary, left_boundary, bottom_boundary, right_boundary):
    if root.no_points == True:
        return []
    if root.is_leaf == True:
        if bottom_boundary <= root.leaf_point[y] <= top_boundary and left_boundary <= root.leaf_point[x] <= right_boundary:
            return [root.leaf_point]
        else:
            return []

    return find_in_nodes(root.node, top_boundary, left_boundary, bottom_boundary, right_boundary)
