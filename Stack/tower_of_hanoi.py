# Uses python call stack. 

def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

counter = 0
def moveDisk(fp,tp):
    global c
    c += 1
    print("moving disk from",fp,"to",tp)

moveTower(8,"A","B","C")
print(counter)
