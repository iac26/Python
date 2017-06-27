#problem 9 Project Euler
import time
n = 1000
s = 0
t = time.time()
def istriplet(a,b,c):
    nums = [a,b,c]
    nums.sort()
    if nums[0]**2 + nums[1]**2 == nums[2]**2:
        return True
    else:
        return False


a = 1
b = a
c = n-(a+b)
while True:
    if c - b < 1:
        a +=1
        b = a
    b += 1
    c = n-(a+b)
    #print a,b,c,a+b+c
    if istriplet(a,b,c):
        s = a*b*c
        break
    if c < 0:
        s = -1
        break
t2 = time.time()-t
print a,b,c
print s
print "solved in",t2,"seconds"
