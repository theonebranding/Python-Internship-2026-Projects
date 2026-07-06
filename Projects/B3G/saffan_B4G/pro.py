import cv2

image1 = cv2.imread(r'C:\Users\Admin\OneDrive\Documents\b3g_safanvahora_py_internship\project\safu.png')

grey_img = cv2.cvtColor(image1 , cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)

blur = cv2.GaussianBlur(invert , (21 ,21),0)
invertBlur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img , invertBlur , scale= 256.0)

cv2.imwrite(r"C:\Users\Admin\OneDrive\Documents\b3g_safanvahora_py_internship\project\safu_sketch.png", sketch)