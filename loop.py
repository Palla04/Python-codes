# 1
x=30
if x<15:
    y=x+15
elif x<=30:
    y=x+30
else:
    y=x

print(y)

# 2
def Hello(choice):
    if choice == 'spam':
        print(1.25)
    elif choice == 'ham':
        print(1.99)
    elif choice == 'eggs':
        print(0.99)
    else:
        print("Bad Choice")

Hello('ham')

# for loop
for i in range(20):
    if(i%3 == 0):
        print(i)
        if(i%5 == 0):
            print('Bingo!')
    print('___')

# While vs For
x=1
while(x<10):
    print(x)
    x=x+1

y=1
for y in range(10):
    print(y)
    y=y+1

x=7
while(x<10):
    if(x>7):
        x+=2
        continue
    x=x+1
    print("Sachin")
    if(x==8):
        break
    print("Tendulkar")

while True:
    reply = input('enter text:')
    if reply == 'stop':
        break
    print(int(reply)**2)
    print("bye")
