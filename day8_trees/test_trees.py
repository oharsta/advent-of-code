from unittest import TestCase

from base import read_lines


class TestTrees(TestCase):

    def test_trees(self):
        def is_edge_tree(all_trees, row, column):
            return row == 0 or row == len(all_trees) - 1 or column == 0 or column == len(all_trees[0]) - 1

        def is_visible(all_trees, row, column, tree):
            if is_edge_tree(all_trees, row, column):
                return True
            left_visible = max([t for i, t in enumerate(all_trees[row]) if i < column]) < tree
            right_visible = max([t for i, t in enumerate(all_trees[row]) if i > column]) < tree
            top_visible = max([all_trees[i][column] for i in range(0, len(all_trees[0])) if i < row]) < tree
            bottom_visible = max([all_trees[i][column] for i in range(0, len(all_trees[0])) if i > row]) < tree
            visible = top_visible or bottom_visible or left_visible or right_visible
            return visible

        def traverse(all_trees, row, column, x_delta, y_delta, tree):
            try:
                yield tree > all_trees[row + x_delta][column + y_delta]
            except IndexError:
                return

        def scenic_score(all_trees, row, column, tree):
            if is_edge_tree(all_trees, row, column):
                return 0
            max_column, max_row = len(all_trees[0]) - 1, len(all_trees) - 1
            left_visible, i = 1, column - 1
            while i > 0 and tree > all_trees[row][i]:
                left_visible += 1
                i -= 1
            right_visible, i = 1, column + 1
            while i < max_column and tree > all_trees[row][i]:
                right_visible += 1
                i += 1
            top_visible, i = 1, row - 1
            while i > 0 and tree > all_trees[i][column]:
                top_visible += 1
                i -= 1
            bottom_visible, i = 1, row + 1
            while i < max_row and tree > all_trees[i][column]:
                bottom_visible += 1
                i += 1
            return left_visible * right_visible * top_visible * bottom_visible

        lines = read_lines("day8_trees/input.txt")

        trees = []
        for line in [l.strip() for l in lines]:
            trees.append([int(tree) for tree in line])

        answer = 0
        for row_nbr, row_of_trees in enumerate(trees):
            for column_nbr, tree in enumerate(row_of_trees):
                if is_visible(trees, row_nbr, column_nbr, tree):
                    answer += 1

        self.assertEqual(1870, answer)

        answer = 0
        for row_nbr, row_of_trees in enumerate(trees):
            for column_nbr, tree in enumerate(row_of_trees):
                score = scenic_score(trees, row_nbr, column_nbr, tree)
                answer = max(score, answer)

        self.assertEqual(517440, answer)
