from PIL import Image
import numpy as np

i = Image.open('images/economist1.jpg')
iar = np.asarray(i)

print iar