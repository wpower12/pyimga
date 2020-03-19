from imgga import TreeBasedRepresentation
from PIL import Image

MAX_DEPTH = 7

f1 = TreeBasedRepresentation.make_individual(MAX_DEPTH)
f2 = TreeBasedRepresentation.make_individual(MAX_DEPTH)
f3 = TreeBasedRepresentation.make_individual(MAX_DEPTH)

size = (256, 256)
X, Y = size
img = Image.new("RGB", size)
pixels = img.load()


def apply_f(f, i, j):
    v = int(f.eval(i, j))
    return max(0, min(255, v))


for i in range(X):
    for j in range(Y):
        r = apply_f(f1, i, j)
        g = apply_f(f2, i, j)
        b = apply_f(f3, i, j)
        pixels[i, j] = (r, g, b)

img.show()
img.close()
