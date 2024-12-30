import cv2
from google.colab.patches import cv2_imshow
import numpy as np

from re import T
img = cv2.imread('Jane.jpg')
if img is None:
  print('Error: The image wasnt loaded. Check the path.')
else:
  img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  suave = cv2.GaussianBlur(img_gray, (7, 7), 0)
  (T, bin) = cv2.threshold(suave, 127, 255, cv2.THRESH_BINARY)

resultado = np.hstack([
    cv2.cvtColor(img, cv2.COLOR_BGR2RGB),
    cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR),
    cv2.cvtColor(bin, cv2.COLOR_GRAY2BGR)
])
cv2_imshow(resultado)
