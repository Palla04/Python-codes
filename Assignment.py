# Sequence Assignment
nudge = 1
wink = 2

A,B = nudge, wink
print(A,B)

C,D = nudge, wink
print(C,D)

nudge=1
wink=2
nudge,wink = wink,nudge
print(nudge,wink)  # Tuples: swaps value

# Multi target assignments:
a=b=c='spam'
print(a,b,c)

a=b=0
b=b+1
print(a,b)