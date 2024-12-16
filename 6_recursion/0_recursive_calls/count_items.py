# a recursive strategy for counting the items in a list
def count_items(list_of_things: list) -> int:
    # base case:  an empty array
    if len(list_of_things) == 0:
      return 0 # turn-around:  an empty list has 0 items

    # break-down:  create an array with 1 fewer items
    list_without_last_item = list_of_things[:-1]
    # recursion:  recursively count items in the smaller list
    previously_counted = count_items(list_without_last_item)
    # build-up:  count the item you removed from the list
    return previously_counted + 1

# use the recursive solution to count items in this list
count_items(['a', 'b', 'c', 'd'])
