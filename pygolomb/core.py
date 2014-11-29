

class Golomb(object):
    """
    Golomb Rice Coding:
    """
    def __init__(self, m):
        from math import ceil, log

        self.m = m
        self.maxbits = int(ceil(log(self.m, 2)))

    def encode(self, n):
        # TODO: log this assertion
        assert isinstance(n, int)

        q, r = divmod(n, self.m)
        return '{0:1>{1}}{2:0>{3}}'.format(0, q + 1, bin(r)[2:], self.maxbits)

    def decode(self, s):
        # TODO: log this assertion
        assert isinstance(s, str)

        zero_pos = s.find('0')
        return (zero_pos * self.m + int(s[zero_pos + 1: zero_pos + 1 + self.maxbits], 2),
                s[zero_pos + 1 + self.maxbits])

class GolombStream(Golomb):
    """
    given streams GolombStream will take care of every thing
    """
    def __init__(self, m, inputstream, outputstream):
        super(GolombStream, self).__init__(m)
        self.inp = inputstream
        self.out = outputstream

    def compress(self):
        s = ''
        while True:
            t = self.inp.read(1)
            if not t:
                break
            s += self.encode(ord(t))
            if len(s) > 8:
                self.out.write(chr(int(s[:8], 2)))
                s = s[8:]
        while s:
            self.out.write(chr(int(s[:8], 2)))
            s = s[8:]

    def decompress(self):
        s = ''
        while True:
            t = self.inp.read(1)
            if not t:
                break
            s += bin(ord(t))[2:]
            n, s = self.decode(s)
            self.out.write(chr(n))
        while s:
            n, s = self.decode(s)
            self.out.write(chr(n))
