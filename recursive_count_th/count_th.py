def count_th(word):
    """Counts the number of 'th' in word(input string). This program is case sensitive

    Arguments:
        word {str} -- the string to be counted

    Returns:
        int -- the number of 'th's found in word
    """
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
