import cv2


img1 = cv2.imread("ozgesu.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Me Original", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

path = 'ozgesu.jpg'
img1 = cv2.imread(path)

blue, green, red = cv2.split(img1)

print("Color values: \n")
print(red,green,blue)


cv2.imshow('Splitted blue',blue)
cv2.imshow('Splitted red', red)
cv2.imshow('Splitted green', green)


me = cv2.merge((blue, green, red))
me1 = cv2.merge((blue, red, green))
me2 = cv2.merge((red, green, blue))

me_mod = cv2.merge((blue+150, green+125, red+20))
me1_mod = cv2.merge((blue-30, red-30, green-30))
me2_mod = cv2.merge((red+5, green+5, blue+5))


cv2.imshow('me red', me)
cv2.imshow('me green', me1)
cv2.imshow('me blue', me2)

cv2.imshow('me red modified', me_mod)
cv2.imshow('me green modified', me1_mod)
cv2.imshow('me blue modified', me2_mod)

cv2.waitKey(0)
cv2.destroyAllWindows()