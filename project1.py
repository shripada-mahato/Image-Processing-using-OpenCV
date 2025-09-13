
## png to jpg image converter ##
# import the OpenCV Library
import cv2

#Read the image by using imread function with the image path under the parentheses
image = cv2.imread(input("Enter Image Link:- "))

# condition applied if the image exits on the file the next proccess are continue
if image is not None:

    # the image is present then show the print statement 
    print("Image Loaded Successfully")

    # imshow function display the image on the screen and the "horse image" statement show top on the image, then called the readed image
    cv2.imshow("Horse Image", image)

    # waitkey(0): that mean until any key press by the user the image are display on the screen
    cv2.waitKey(0)

    # destroyALLwindows: destroy all the other windows and show the image on the top
    cv2.destroyAllWindows()

    # if we need to save the particulur image then use the imwrite() function with their image extension name then called the image
    cv2.imwrite("Horse_image1.jpg",image)

    # if the all proccess are complete then we show the confirmation massage on the screen
    print("Image Convert Successfully png => jpg")
    
    # if image is not Loaded then print the below statement
else:
    print("Image Could't Found")