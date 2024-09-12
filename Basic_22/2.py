def remove(List):
    i=2
    while len(List) > 0:
        i = i % len(List)
        print("Romove: ", List.pop(i))

        i=i+2  #Reset the index


List = [1,2,3,4,5,6,7,8,9]
remove(List)