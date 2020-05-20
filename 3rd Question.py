#. Given a Python list, remove all the even number from the list and
# save those even number in another list and print both the lists.
#For a given input list:  List1 = [1,2,3,4,5,6,7]
                        #Output : List1=[1,3,5,7]
                        #List2 = [2,4,6]
def Split(A):
    evenlist = []
    oddlist = []
    for i in A:
        if (i % 2 == 0):
            evenlist.append(i)
        else:
            oddlist.append(i)
    print("List1:", oddlist)
    print("List2:", evenlist)
A = [1,2,3,4,5,6,7]
Split(A)
