from imgga import InstructionListRepresentation
from PIL import Image

NUM_INSTRUCTIONS = 30
size = (256, 256)
X, Y = size
img = Image.new("RGBA", size, color="white")
pixels = img.load()

explicit_i = InstructionListRepresentation.make_individual(NUM_INSTRUCTIONS, X, Y)
explicit_i.eval(img)

img.show()
img.close()
