#
# Problem: Given a squared matrix, print it in a spiral form.
#
# Given:
#       M = A B C
#           D E F
#           G H I
# Return:
#       > A D G H I F C B E
#
#
# Bonus: The same, but the matrix is in a list.
#
# Given:
#       M = A B C D E F G H I
# Return:
#       > A D G H I F C B E
#


M3 = [['A', 'B', 'C'],
      ['D', 'E', 'F'],
      ['G', 'H', 'I']]
SP3 = 'ADGHIFCBE'
L3  = 'ABCDEFGHI'

M4 = [['A', 'B', 'C', 'D'],
      ['E', 'F', 'G', 'H'],
      ['I', 'J', 'K', 'L'],
      ['M', 'N', 'O', 'P']]
SP4 = 'AEIMNOPLHDCBFJKG'
L4  = 'ABCDEFGHIJKLMNOP'

M5 = [['A', 'B', 'C', 'D', 'E'],
      ['F', 'G', 'H', 'I', 'J'],
      ['K', 'L', 'M', 'N', 'O'],
      ['P', 'Q', 'R', 'S', 'T'],
      ['U', 'V', 'W', 'X', 'Y']]
SP5 = 'AFKPUVWXYTOJEDCBGLQRSNIHM'
L5  = 'ABCDEFGHIJKLMNOPQRSTUVWXY'

def spiral_matrix_print(M, bonus=False):
    if bonus:
        C = int(len(M) ** (0.5))
    else:
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

    solution = ''

    while ci < T:
        if bonus:
            solution += M[j * C + i]
        else:
            solution += M[j][i]
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

    return solution

def test(test_func):
    tests = [('M3', M3, SP3), ('M4', M4, SP4), ('M5', M5, SP5)]
    for (t,m,l) in tests:
        print "%s: %s (%s)" % (t, test_func(m) == l, test_func(m))

def _list_to_matrix(L):
    c = int(len(L) ** (0.5))
    M = []
    for i in range(0, len(L), c):
        M.append(L[i:i+c])
    return M

def bonus2(L):
    # Convert the list to a matrix
    return spiral_matrix_print(_list_to_matrix(L))

def bonus(L):
    # Use a mapping between the list and the matrix
    return spiral_matrix_print(L, bonus=True)

def test_bonus(test_func):
    tests = [('L3', L3, SP3), ('L4', L4, SP4), ('L5', L5, SP5)]
    for (t,m,l) in tests:
        print "%s: %s (%s)" % (t, test_func(m) == l, test_func(m))

if __name__ == '__main__':
    test(spiral_matrix_print)
    test_bonus(bonus)
