my_set={1,2,3}
my_set.add(4)           # to add element to the last in the set
print(my_set)
my_set.remove(1)        # to remove element from the set(raises error if the element is not present)
my_set.discard(5)       # to remove element from the set without raising error
print(my_set)
my_set1={5,6}
a=my_set.union(my_set1)        # to add two set
print(a)