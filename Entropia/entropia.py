from bitarray import *
import math

def addprefixos(xs, p):
    return dict((k, bitarray(p) + v) for (k,v) in xs.items())

class N:
    def __init__(self, x, f):
        self.x = x
        self.f = f
        self.l = None
        self.r = None

    def join(self, o):
        n = N(None, self.f + o.f)
        n.l = self
        n.r = o
        return n

    def coding(self):
        l = {}
        r = {}
        if self.x:
            return {self.x: bitarray()}
        if self.l:
            l = self.l.coding()
        if self.r:
            r = self.r.coding()
        ret = {}
        ret.update(addprefixos(l, '0'))
        ret.update(addprefixos(r, '1'))
        return ret

    def __lt__(self, o):
        return self.f > o.f

    def __repr__(self):
        return "N('%s',%d)" % (self.x, self.f)

def huffmann(l):
    while(len(l) > 1):
        l.sort()
        a = l.pop()
        b = l.pop()
        c = a.join(b)
        l.append(c)
    return l.pop().coding()

def countT(txt):
    l = {}
    for i in txt:
        if i in l:
            l[i] += 1
        else:
            l[i] = 1
    return l

def createNode(lista):
    l = []
    for x, j in lista.items():
        l.append(N(x,j))
    return l

def countF(lista):
    total = 0
    for x,j in lista.items():
        total = total + j
    return total

def countE(k):
    total = 0
    for x, j in k.items():
        intro = j / countF(k)
        total = total + (intro * (math.log(intro,256)))
    return -total

def coddingFile(file):
    dfrequencia = countT(file)
    l = createNode(dfrequencia)
    dic = huffmann(l)
    k = bitarray()
    for i in file:
        k += dic[i]
    return k

def decoddingFile(txt, chave):
    k = {}
    a = txt.to01()
    for i,j in chave.items():
        k[j.to01()] = i
    l = []
    n = ""
    i = 0
    j = 1
    while(1):
        n = a[i:j]
        if n in k:
            l.append(k[n])
            i = j
            j += 1
        else:
            j +=1
        if j == (len(a) -1):
            break
    return l

# Arquivos para a execuçao:
textOriginal = open("in.txt", 'rb').read()
outOriginal = open("out.txt", 'wb')

# Execuçao da Entropia:
dfrequencia = countT(textOriginal)
dEntro = countE(dfrequencia)
print("Entropia do Arquivo Original: ", dEntro)
l = createNode(dfrequencia)
j = coddingFile(textOriginal)
x = decoddingFile(j, huffmann(l))
outOriginal.write(j.tobytes())
outOriginal.close()

outCompact = open("outCompact.txt", 'wb')
outCompact.write(bytes(x))
textCompact = open("out.txt", "rb").read()
dfrequencia = countT(textCompact)
dEntro = countE(dfrequencia)
print("Entropia do Arquivo Compactado: ", dEntro)
