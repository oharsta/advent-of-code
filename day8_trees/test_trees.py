from unittest import TestCase

from base import read_lines


class TestTrees(TestCase):

    def test_trees(self):
        trees = [[int(tree) for tree in line] for line in [l.strip() for l in read_lines("day8_trees/input.txt")]]
        nbr_rows = len(trees)
        nbr_columns = len(trees[0])

        def adjacent_tree_length(tree_instance, xaxis, yaxis, move, count=0):
            x, y = xaxis + move[0], yaxis + move[1]
            within_bounds = -1 < x < nbr_rows and -1 < y < nbr_columns
            if within_bounds and trees[x][y] < tree_instance:
                return adjacent_tree_length(tree_instance, x, y, move, count=count + 1)
            return [count, count + 1 if within_bounds else count]

        visible_trees, scenic_score = 0, 0
        moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for row in range(nbr_rows):
            for column in range(nbr_columns):
                tree = trees[row][column]
                up, right, down, left = [adjacent_tree_length(tree, row, column, move) for move in moves]
                free_row_view = up[0] == row or nbr_rows - 1 == row + down[0]
                free_column_view = nbr_columns - 1 == column + right[0] or column - left[0] == 0
                if free_row_view or free_column_view:
                    visible_trees += 1
                scenic_score = max(scenic_score, up[1] * right[1] * down[1] * left[1])

        self.assertEqual(1870, visible_trees)
        self.assertEqual(517440, scenic_score)
