def add(x, y = 6):
    return x + y
print(add(12, 13))
print(add(15))

def Alarm(h = 6, m = 30, s = 0):
    print"Wake UP! It is {0}:{1}:{2}".format(h, m, s)
Alarm(m = 0, s = 30, h = 4)
Alarm()
Alarm(5)
Alarm(6, 20)
Alarm(7, 30, 45)
