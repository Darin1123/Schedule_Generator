import Point as pt 

p1 = pt.Point(1, 2)
p2 = pt.Point(1, 2)

#print(p1.compareTo(p2))

s1 = set()
s1.add(p1)

s2 = set()
s2.add(p2)

s3 = s1&s2

print(s3)
