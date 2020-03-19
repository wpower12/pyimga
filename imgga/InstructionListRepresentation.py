import math
import random
from PIL import Image, ImageDraw, ImageColor


# - "List of Explicit Instructions" Representation
INSTRUCTION_TYPES = ["R", "C", "A", "E", "L"]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    a = random.randint(0, 255)
    # return ImageColor.getrgb("rgb({},{},{})".format(r, g, b))
    return r, g, b, a


class InstructionList:

    def __init__(self):
        self.instruction_list = []

    def eval(self, img: Image):
        dc = ImageDraw.Draw(img)

        for i in self.instruction_list:
            # Parse i, apply operation to image
            kind = i[0]

            # Rectangle
            if kind == "R":
                xy = i[1]
                fill_color = i[2]
                dc.rectangle(xy, fill=fill_color)

            # Ellipse
            if kind == "E":
                xy = i[1]
                fill_color = i[2]
                dc.ellipse(xy, fill=fill_color)

            # Line
            if kind == "L":
                xy = i[1]
                width = i[2]
                fill_color = i[3]
                dc.line(xy, width=width, fill=fill_color)


def make_individual(num_instructions, max_h, max_w):
    ind = InstructionList()
    for i in range(num_instructions):
        kind = random.choice(INSTRUCTION_TYPES)

        # Rectangle
        if kind == "R":
            # Choose 4 points within the
            MAX_W = 10
            x1 = random.randrange(0, max_w - 1)
            x2 = random.randrange(x1 + 1, max_w)
            y1 = random.randrange(0, max_h - 1)
            y2 = random.randrange(y1 + 1, max_h)
            ind.instruction_list.append(["R", ((x1, y1), (x2, y2)), random_color()])

        if kind == "C":
            # choose a radius
            r = random.randrange(0, int(0.05 * (min(max_h, max_w))))
            x_c = random.randrange(r, max_w - r)
            y_c = random.randrange(r, max_h - r)
            ind.instruction_list.append(["E", (x_c - r, y_c - r, x_c + r, y_c + r), random_color()])

        if kind == "L":
            x1 = random.randrange(0, max_w - 1)
            x2 = random.randrange(0, max_w)
            y1 = random.randrange(0, max_h - 1)
            y2 = random.randrange(0, max_h)
            width = random.randint(1,10)
            ind.instruction_list.append(["L", ((x1, y1), (x2, y2)), width, random_color()])

        if kind == "E":
            # Choose 4 points
            x1 = random.randrange(0, max_w - 1)
            x2 = random.randrange(x1 + 1, max_w)
            y1 = random.randrange(0, max_h - 1)
            y2 = random.randrange(y1 + 1, max_h)
            ind.instruction_list.append(["E", ((x1, y1), (x2, y2)), random_color()])

    return ind