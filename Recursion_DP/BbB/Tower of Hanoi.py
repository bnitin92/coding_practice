# tower of hanoi

"""
Abdual bari explaination

if n > 0

move all n - 1 disks from A to B using C
move the nth disk from A to C
move all n - 1 disks from B to C using A

from to and aux rods will change accordingly in sub problems
"""

# its 2 ^ n cha=eck how

def towerofHanoi(n, from_rod, to_rod, aux_rod):
    # if n == 1:
    #     print("Move Disk 1 from "+ from_rod + " to " + to_rod)
    #     return

    if n > 0:
        towerofHanoi(n-1, from_rod, aux_rod, to_rod)
        print("Move Disk " + str(n) + " from " + from_rod + " to " + to_rod)
        towerofHanoi(n-1, aux_rod, to_rod, from_rod)

print(towerofHanoi(10, "A", "C", "B"))