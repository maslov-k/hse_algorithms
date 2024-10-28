from collections import defaultdict
import sys


def relationship(adj_lists, start, finish, rel_type=-1):
    for v in adj_lists[start]:
        cur_rel_type = v[1]
        if cur_rel_type == rel_type or rel_type == -1:
            current_ind = v[0]
            if current_ind == finish:
                return cur_rel_type
            else:
                result = relationship(adj_lists, current_ind, finish, cur_rel_type)
                if result > 0:
                    return result

    return 0


def main():
    n = int(sys.stdin.readline())

    adj_lists = defaultdict(list)

    names_ids = defaultdict(lambda: len(names_ids))

    for i in range(n - 1):
        child, parent = sys.stdin.readline().split()
        child_index = names_ids[child]
        parent_index = names_ids[parent]

        adj_lists[child_index].append((parent_index, 2))
        adj_lists[parent_index].append((child_index, 1))

    for line in sys.stdin:
        name_1, name_2 = line.split()
        print(relationship(adj_lists, names_ids[name_1], names_ids[name_2]), end=' ')


if __name__ == '__main__':
    main()
