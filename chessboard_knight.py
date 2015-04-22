#!/usr/bin/env python

# Given a matrix A (NxM) of 0 and 1, return the minimun number of moves a Knight takes
# to moves from upper-left(0,0) to lower-right(N-1,M-1). The knight can only walk in 0's, 1's are blocked.
# return -1 if it cannot make it.
# O(N*M) time
# O(N*M) space


# return the posible moves that the knight in pos (x, y) can do.
# excluding invalid positions, blocked squares and visited squares.
def get_moves(x, y, A, N, M, visited):
    posibles_moves = [(x-2, y-1), (x-2, y+1),
                      (x-1, y-2), (x-1, y+2),
                      (x+1, y-2), (x+1, y+2),
                      (x+2, y-1), (x+2, y+1)]

    final_moves = [(i,j) for (i,j) in posibles_moves if (0<=i and i<N and 0<=j and j<M and A[i][j] == 0 and (i,j) not in visited)]
    return final_moves


def solution(A):
    from collections import deque
    N = len(A)
    M = len(A[0])

    visited = {}
    next_steps = deque()

    start = (0,0)
    final_pos = (N-1, M-1)
    next_steps.append((start, 0)) # (next_move, steps_given)

    while True:
        try:
            cur_pos, steps = next_steps.popleft()
        except IndexError as e: # no more moves to try, not possible to arrive
            return -1

        if cur_pos == final_pos: # arrived
            return steps
        else:
            visited[cur_pos] = True
            moves = get_moves(cur_pos[0], cur_pos[1], A, N, M, visited)
            for m in moves:
                next_steps.append((m, steps+1))



if __name__ == '__main__':
    t1 = [[0,0,0], [0,0,1], [1,0,0], [0,0,0]]
    t2 = [[0,0,0], [0,0,0], [0,0,0], [0,0,0]]
    t3 = [[0,0,0], [0,0,0], [0,0,0]]
    t4 = [[0,0], [0,0]]
    t5 = [[0]]
    print solution(t1) == 7
    print solution(t2) == 3
    print solution(t3) == 4
    print solution(t4) == -1
    print solution(t5) == 0

