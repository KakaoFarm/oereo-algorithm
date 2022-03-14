"""
이 문제는 함수 재귀로 접근하는 순간 recursion error 발생
임의로 setrecursionlimit을 늘렸더니 메모리 초과 에러 발생
그렇다면 재귀가 아닌 queue로 재귀를 구현해보자!!
"""
# import sys

# sys.setrecursionlimit(10 ** 6)
tree_nums = []

while True:
    try:
        num = int(input())
        tree_nums.append(num)
    except:
        break


# print(tree_nums)


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    def post_order_traversal(self):
        # print(self.root.data)
        result = []

        def _post_order_traversal(root):
            queue = []
            queue.append(root)

            while queue:
                root = queue.pop()
                if root is None:
                    pass
                else:
                    queue.append(root.left)
                    queue.append(root.right)
                    result.append(root.data)

        _post_order_traversal(self.root)
        return result


bst = BinarySearchTree()
for num in tree_nums:
    bst.insert(num)

result = bst.post_order_traversal()
# print(result)
for i in range(len(result)-1, -1, -1):
    print(result[i])