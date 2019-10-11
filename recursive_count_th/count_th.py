'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # if word is an empty string return 0
    if len(word) == 0:
        return 0

    # initialize a variable count to 0
    count = 0

    # create a function count_th_number to take position as argument
    def count_th_number(pos):

        # state a base case of position >= len(word) - 1
        # if it is return
        if pos >= len(word) - 1:
            return

        # if current position is a 't' and next position is a 'h'
        # increment count by 1 and call count_th_number with position + 2
        if word[pos] == 't' and word[pos + 1] == 'h':
            # because an int is passed as value
            # use the nonlocal keyword so this function can use count in closure space
            nonlocal count
            count += 1
            count_th_number(pos + 2)

        # else call count_th_number with position + 1
        else:
            count_th_number(pos + 1)

    # call count_th_number with position 0
    count_th_number(0)

    # return count
    return count
