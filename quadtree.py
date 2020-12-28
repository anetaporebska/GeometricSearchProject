import math


northeast = top = x = 0
northwest = left = y = 1
southwest = bottom = 2
southeast = right = 3


class Node:
    def __init__(self, top_boundary, left_boundary, bottom_boundary, right_boundary):
        self.boundaries = (top_boundary, left_boundary, bottom_boundary, right_boundary)
        self.children = [None, None, None, None]
        self.is_children_leaf = [False, False, False, False]


class Root:
    def __init__(self, no_points, is_leaf, leaf_point, node):
        self.no_points = no_points
        self.is_leaf = is_leaf
        self.leaf_point = leaf_point
        self.node = node


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
            parent.is_children_leaf[child_index] = True

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


def create_root(points):
    left_boundary, right_boundary, bottom_boundary, top_boundary = found_boundaries(points)

    if len(points) == 0:
        return Root(True, False, None, None)
    if len(points) == 1:
        return Root(False, True, points[0], None)

    return Root(False, False, None, Node(top_boundary, left_boundary, bottom_boundary, right_boundary))


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


def find_in_nodes(parent, top_boundary, left_boundary, bottom_boundary, right_boundary):
    points_inside = []
    for child_index in range(4):
        if parent.is_children_leaf[child_index]:
            child = parent.children[child_index]
            if bottom_boundary <= child[y] <= top_boundary and left_boundary <= child[x] <= right_boundary:
                points_inside.append(child)

        elif parent.children[child_index] != None:
            child = parent.children[child_index]
            if field_inside(child, top_boundary, left_boundary, bottom_boundary, right_boundary):
                points_inside += find_in_nodes(child, top_boundary, left_boundary, bottom_boundary, right_boundary)

    return points_inside


def find_points(root, top_boundary, left_boundary, bottom_boundary, right_boundary):
    if root.no_points == True:
        return []
    if root.is_leaf == True:
        if bottom_boundary <= root.leaf_point[y] <= top_boundary and left_boundary <= root.leaf_point[x] <= right_boundary:
            return [root.leaf_point]
        else:
            return []

    return find_in_nodes(root.node, top_boundary, left_boundary, bottom_boundary, right_boundary)


def prepare_tree(points):
    root = create_root(points)

    if root.no_points == False and root.is_leaf == False:
        prepare_next_nodes(root.node, points)

    return root


#"""
points = [(5.3, 5.2), (5.3, 6.7), (6.0, 8.4), (6.3, 8.9), (7.3, 8.4000001), (8.85, 8.83), (8.82767, 7.8),
          (8.82767, 5.9), (8.82767, 5.59), (8.82767, 5.588), (7, 7), (7.2, 7.4), (8, 6.5), (7.499999, 5.49999), (6, 4),
          (6.2, 3.6), (8.9, 3.9), (0.44213512, 5.12532), (0.14144, 3.51), (1.2, 1.251)]
top_boundary = 8.4
left_boundary = 6
bottom_boundary = 4
right_boundary = 8.82767

tree = prepare_tree(points)
result = find_points(tree, top_boundary, left_boundary, bottom_boundary, right_boundary)

print(result)
#"""
