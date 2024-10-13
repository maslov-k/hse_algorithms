def depth(tree, name):
    parent_depth = tree[name][1]

    if parent_depth != -1:
        return parent_depth + 1
    elif not tree[name][0]:
        return 0

    return depth(tree, tree[name][0]) + 1


def main():
    n = int(input())

    family_tree = {}
    root = ''

    for _i in range(n - 1):
        [child, parent] = input().split()

        if not root or child == root:
            root = parent

        if parent not in family_tree:
            family_tree[parent] = ('', -1)

        family_tree[child] = (parent, -1)

    for name in sorted(family_tree.keys()):
        print(name, depth(family_tree, name))


if __name__ == '__main__':
    main()
