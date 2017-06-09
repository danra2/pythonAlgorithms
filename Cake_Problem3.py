# list_of_ints = [3,5,1,2,7,2]
# list_of_highest_integers = []
#
# def highest_product_three_ints(list_of_ints):
#
#     current_max_value = list_of_ints[0]
#     max_product_value = list_of_highest_integers[1] * list_of_highest_integers[2] * list_of_highest_integers[3]
#
#
#     while i < len(list_of_ints):
#         highest_single_value = max(current_max_value, current_index_value)
#
#         if (i = len(list_of_ints)-1)
#             list_of_ints.pop(highest_single_value)
#             list_of_highest_integers.push(highest_single_value)
#             highest_single_value = list_of_ints[0]
#
#         if len(list_of_ints) < 3:
#             raise IndexError('Requires minimum of at least three integers.')
#
#         else
#             return max_product_value


from itertools import islice

def highest_product_of_3(list_of_ints):
    if len(list_of_ints) < 3:
        raise Exception('Less than 3 items!')

    # We're going to start at the 3rd item (at index 2)
    # so pre-populate highests and lowests based on the first 2 items.
    # we could also start these as None and check below if they're set
    # but this is arguably cleaner
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest =  min(list_of_ints[0], list_of_ints[1])

    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2  = list_of_ints[0] * list_of_ints[1]

    # except this one--we pre-populate it for the first *3* items.
    # this means in our first pass it'll check against itself, which is fine.
    highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    # walk through items, starting at index 2
    for current in islice(list_of_ints, 2, None):

        # do we have a new highest product of 3?
        # it's either the current highest,
        # or the current times the highest product of two
        # or the current times the lowest product of two
        highest_product_of_3 = max(
            highest_product_of_3,
            current * highest_product_of_2,
            current * lowest_product_of_2)

        # do we have a new highest product of two?
        highest_product_of_2 = max(
            highest_product_of_2,
            current * highest,
            current * lowest)

        # do we have a new lowest product of two?
        lowest_product_of_2 = min(
            lowest_product_of_2,
            current * highest,
            current * lowest)

        # do we have a new highest?
        highest = max(highest, current)

        # do we have a new lowest?
        lowest = min(lowest, current)

    return highest_product_of_3
