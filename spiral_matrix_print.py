#
# Problem: Given a squared matrix, print it in a spiral form.
#
# Given:
#       M = A B C
#           D E F
#           G H I
# Print:
#       > A D G H I F C B E


def spiral_matrix_print(M):
    C = len(M)

    i = 0; j = 0 # Index to print

    # Internal limit to stop printing, by side
    fd = C - 1
    fu = 0
    fl = 0
    fr = C - 1

    T = C * C # Total number of element to print
    ci = 0    # Actual number of element printed
    d = 'd'   # Direction of movement: u,d,l,r

    solution = []

    while ci < T:
        solution.append(M[j][i])
        ci += 1

        if d == 'd':   # down
            if j >= fd:
                d  = 'r'
                fl += 1
                i  += 1
            else:
                j += 1

        elif d == 'r': # right
            if i >= fr:
                d  = 'u'
                fd -= 1
                j  -= 1
            else:
                i += 1

        elif d == 'u': # up
            if j <= fu:
                d  = 'l'
                fr -= 1
                i  -= 1
            else:
                j -= 1

        elif d == 'l': # left
            if i <= fl:
                d  = 'd'
                fu += 1
                j  += 1
            else:
                i -= 1

    print ' '.join(solution)


M3 = [['A', 'B', 'C'],
      ['D', 'E', 'F'],
      ['G', 'H', 'I']]

M4 = [['A', 'B', 'C', 'D'],
      ['E', 'F', 'G', 'H'],
      ['I', 'J', 'K', 'L'],
      ['M', 'N', 'O', 'P']]

M5 = [['A', 'B', 'C', 'D', 'E'],
      ['F', 'G', 'H', 'I', 'J'],
      ['K', 'L', 'M', 'N', 'O'],
      ['P', 'Q', 'R', 'S', 'T'],
      ['U', 'V', 'W', 'X', 'Y']]

spiral_matrix_print(M3)
spiral_matrix_print(M4)
spiral_matrix_print(M5)
