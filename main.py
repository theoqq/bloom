def count(start=1, step=1):
    counter = start
    while True:
        yield counter
        counter += step


