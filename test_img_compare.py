from imgga import InstructionListRepresentation
from PIL import Image
import scipy.spatial.distance as dist
import numpy as np

# Get Input Image
img_target = Image.open("lena.png", 'r').convert("RGBA")
pixels_target = np.asarray(img_target)

# Build Random Image
NUM_INSTRUCTIONS = 30
size = img_target.size
X, Y = size
img_random = Image.new("RGBA", size, color="white")
pixels = img_random.load()

explicit_i = InstructionListRepresentation.make_individual(NUM_INSTRUCTIONS, X, Y)
explicit_i.eval(img_random)

pixels_random = np.asarray(img_random)

d = dist.euclidean(pixels_target.flatten(), pixels_random.flatten())
print(d)
