
def Intersection(list_1,list_2):

        intersection = []
        for i in list_1:
            for j in list_2:
                if i == j:
                    intersection.append(i)
        
        return intersection


list_1 = [1,4,6,9]
list_2 = [3,6,8,9]

result = Intersection(list_1,list_2)
print("The intersection between the two lists is:", result)
