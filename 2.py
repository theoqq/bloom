def besk():
    a=1
    while True:
        a+=1
        yield a
print (besk())
