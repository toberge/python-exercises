#!/usr/bin/env python3
import os
import time

"""
Conway's game of life
dead: live if neighbours == 3
alive: live if neighbours in {2,3}
else stay dead or die.

TODO: fix wrap-around (currently negative values)
"""

COLS, ROWS = os.get_terminal_size()

def points_from_grid(grid, offset=(0,0)):
    points = set()
    x0, y0 = offset
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            if cell == 'X':
                points.add((x0+x,y0+y))
    return points

def disp_grid(points):
    grid = []
    for i in range(ROWS):
        grid.append(['.'] * COLS)
    for point in points:
        x, y = point
        grid[y][x] = 'X'
    print('\n'.join(''.join(s) for s in grid), end='')

def count_neighbours(point, points):
    # TODO this ain't needed
    x, y = point
    count = 0
    for candidate in [(x-1,y),(x+1,y),(x-1,y-1),(x+1,y-1),(x+1,y+1),(x-1,y+1),(x,y+1),(x,y-1)]:
        if candidate in points:
            count += 1
    return count

def identify_neighbours(point, points):
    """Return dead, alive"""
    x, y = point
    neighbours = {(x-1,y),(x+1,y),(x-1,y-1),(x+1,y-1),(x+1,y+1),(x-1,y+1),(x,y+1),(x,y-1)}
    return neighbours.difference(points), neighbours.intersection(points)

def tick(points):
    dying = set()
    born = set()
    for point in points:
        # get those neighbours sorted
        dead, alive = identify_neighbours(point, points)
        # Apply rule 1-3
        if not 1 < len(alive) < 4:
            dying.add(point)
        for point in dead: # see if any dead should rise
            # Apply rule 4
            if count_neighbours(point, points) == 3:
                born.add(point)
    # return alive - dying + born
    return points.difference(dying).union(born)

if __name__ == "__main__":
    #points = {(1,2), (3,4), (4,4), (4,3), (4,5), (4,6), (4,7), (4,8)}
    points = points_from_grid([
        '.XXX.X..',
        '.X......',
        '....XX..',
        '..XX.X..',
        '.X.X.X..',
    ], offset=(4,4))
    try:
        while True:
            disp_grid(points)
            time.sleep(1)
            points = tick(points)
    except KeyboardInterrupt:
        print(points)