from unittest import TestCase

from base import read_lines


class TestDiskSpace(TestCase):

    def test_disk_space(self):
        lines = read_lines("day7_disk_space/input.txt")

        files = {}
        paths = []
        for line in [l.strip() for l in lines]:
            commands = line.split()
            if commands[0] != "dir" and commands[1] != "ls":
                if commands[1] == "cd":
                    if commands[2] != "..":
                        paths.append(commands[2])
                    else:
                        paths.pop()
                else:
                    size = int(commands[0])
                    for index, _ in enumerate(paths):
                        path = "/".join(paths[:index + 1])
                        accumulated_size = files.get(path, 0)
                        files[path] = accumulated_size + size

        answer = sum([size for size in files.values() if size <= 100000])
        self.assertEqual(1667443, answer)

        total, required, used = (70_000_000, 30_000_000, files["/"])
        minimal_dir_size = used + required - total
        answer = min([size for size in files.values() if size >= minimal_dir_size])
        self.assertEqual(8998590, answer)
