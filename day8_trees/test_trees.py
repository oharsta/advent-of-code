from unittest import TestCase

from base import read_lines


class TestTrees(TestCase):

    def test_trees(self):
        trees = [[int(tree) for tree in line] for line in [l.strip() for l in read_lines("day8_trees/input.txt")]]
        nbr_rows = len(trees)
        nbr_columns = len(trees[0])

        def adjacent_trees(tree_instance, xaxis, yaxis, move, res=[]):
            x, y = xaxis + move[0], yaxis + move[1]
            within_bounds = -1 < x < nbr_rows and -1 < y < nbr_columns
            if within_bounds and trees[x][y] < tree_instance:
                return adjacent_trees(tree_instance, x, y, move, res=res + [trees[x][y]])
            res_scenic = res + [trees[x][y]] if within_bounds else res
            return [res, res_scenic]

        visible_trees, scenic_score = 0, 0
        moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for row in range(nbr_rows):
            for column in range(nbr_columns):
                tree = trees[row][column]
                up, right, down, left = [adjacent_trees(tree, row, column, move) for move in moves]
                free_row_view = len(up[0]) == row or nbr_rows - 1 == row + len(down[0])
                free_column_view = nbr_columns - 1 == column + len(right[0]) or column - len(left[0]) == 0
                if free_row_view or free_column_view:
                    visible_trees += 1
                scenic_score = max(scenic_score, len(up[1]) * len(right[1]) * len(down[1]) * len(left[1]))

        self.assertEqual(1870, visible_trees)
        self.assertEqual(517440, scenic_score)
