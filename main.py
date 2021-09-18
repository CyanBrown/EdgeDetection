from PIL import Image
import numpy as np
from edgedetection import edge_detection

pimg = Image.open("examples/download.jpg").convert("L")

# this can be used to decrease processing times
# pimg = pimg.resize((int(pimg.size[0]*.5), int(pimg.size[1]*.5)), Image.ANTIALIAS)

aimg = np.array(pimg, dtype=np.uint8)

nimg = edge_detection(aimg)

Image.fromarray(nimg).save("product6.png")
