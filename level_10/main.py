# http://www.pythonchallenge.com/pc/return/bull.html (huge:file)

def gen(n):
    a = '1'
    yield '1'
    for i in range(n):
        b = []
        count, char = 1, a[0]
        for i in range(1, len(a)):
            if a[i] == char:
                count += 1
            else:
                b.append('%d%s' % (count, char))
                count, char = 1, a[i]
        b.append('%d%s' % (count, char))
        a = ''.join(b)
        yield a

print(len(list(gen(30))[-1]))