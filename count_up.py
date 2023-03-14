def count_up(start, stop):

    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """
    actual_stop = stop + 1

    x = range(start,actual_stop)

    for n in x:
        print(n)
    # YOUR CODE HERE


count_up(5, 7)        


count_up(4,10)

