import cv2

image = cv2.imread(input("Enter the image link:- "))
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

w, h, c = image.shape
print(f"Width:-{h}\nHeight:-{w}\nchannel:-{c}")

total_pixel = w * h

print(f"Total number of pixel:- {total_pixel}")
