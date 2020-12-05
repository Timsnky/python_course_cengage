def myRange(start, stop=None, step=None):
    if not stop:
        return myRange(0, start)

    if not step:
        return myRange(start, stop, 1)

    data = []
    if step > 0:
        while start < stop:
            data.append(start)
            start += step
    else:
        while start > stop:
            data.append(start)
            start += step

    return data


myRange(10)