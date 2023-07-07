#
# deque - hybrid object between stack and queue
#
# - Deque objects are like double-ended queues
# - Double-ended queue, pronounced "deck"
# - Deque is memory efficient, we can access data from either end
#   d = collections.deque('abcdefg')
#   appendLeft() # append from left
#   append()     # append from right
#   popleft()    # remove from left
#   pop()        # remove from right
#   rotate()     # positive to the right, negative to the left
#

import collections
import string


def main():
    # initialize a deque with lowercase letters
    d = collections.deque(string.ascii_lowercase)

    # deques support the len() function
    print("Item count: ", str(len(d)))   # Item count:  26
    
    # deques can be iterated over
    for elem in d:
        print(elem.upper(), end=",")
        
    print()
    
    # manipuate items from either end
    a = d.pop()
    b = d.popleft()
    d.append(2)
    d.appendleft(1)
    print(a) # z
    print(b) # a
    print(d) # deque([1, 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 2])

    # rotate the deque
    # rotate means that put the bottom elements to top
    # eg: rotate 1 indicates that the 1 value of the deque goes from the end to the front
    # use case: restaurant sign-up list
    print(d) # deque([1, 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 2])
    d.rotate(10)
    print(d) # deque(['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 2, 1, 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'])


if __name__ == "__main__":
    main()
