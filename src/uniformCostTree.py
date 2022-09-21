# Contains Uniform Cost Tree Search Algorithm
from vacuum import Vacuum

#iterates through the room and finds all the dirty rooms and put them in the dirty room. 
#array 2x the size of the amount of dirty rooms: x,y


def findDirtyRooms(map):
    for ir, row in enumerate(map):
        for ic, col in enumerate(row):
            map[ir][ic]= ir+ic
            # print("row = ", row, "col = ", col, "total", ir+ic)
        print(row)

    # rowLocation = -1
    # colLocation = -1
    # for row in map:
    #     rowLocation +=1
    #     colLocation = -1
    #     for room in row:
    #         colLocation +=1
    #         # if room == 1: 
    #         print("row =", rowLocation)
    #         print("col =",  colLocation)
    #         print("location =", map[rowLocation][colLocation])

map = [[0 for i in range(5)] for j in range(4)]
map[0][0] = 1
map[3][4] = 1
print(map)
findDirtyRooms(map)
print(map)

print("its happeneing")
for row in map:
    print(row)