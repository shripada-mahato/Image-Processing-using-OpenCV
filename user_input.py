
# image operation using OpenCV

# import opencv library as cv2
import cv2

# create a variable and use imread() function to read the image by using input method as the image link
image = cv2.imread(input("Enter the image link:- "))

# used conditional statement cheaked the image link valid or not
# if the link is valid then execute this portion
if image is not None:

    # imshow() method used to display the picture on the screen
    cv2.imshow(input("Enter The Image Title Name:- "), image)

    # waitKey() method used until the picture dispaly on the screen, until any key press from the keyboard
    cv2.waitKey(0)

    # destroyAllWindows() used destroy other all windows
    cv2.destroyAllWindows()

# after that open option windows, choose the option according to the need
# 1. save the image, 2. convert the image, 3. Exit from the operation
    print("\n Choose The Option:- ")
    print("1. save the image- ")
    print("2. convert the image- ")
    print("3. Exit-")

# Choose the option according to the need
    choise = input("Enter the choise (1 or 2 or 3):- ")

    # if choose the option 1 then execute this portion
    if choise == '1':
        save = input("enter file name to save")

        # imwrite() method used to save the picture
        cv2.imwrite(save, image)
        print("Image Saved successfully")

    # if chhose option 2 then execute this portion
    elif choise == '2':

        # if we need to save the  picture then enter the image name with their extension ex(hello.png)
        # by using input() method
        save = input("Enter the file Name (e.g Hello.png):- ")

        # cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), use this method to save the picture black and white
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # after that save the black & white image into the save variable
        cv2.imwrite(save, gray)

        # after all of the operation show the successfull operaftion
        print("Image Convert Successfully Colorful => Black & White")
        cv2.imshow("image", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        exit()

    # if choose option 3 execute this option
    elif choise == '3':
        print("Operation Exit Successfully...!")
        exit()
    else:
        print("Invalid Operation...")

# if the user enter invalid link then execute this portion
else:
    print("Error..! Invalid Image")
    