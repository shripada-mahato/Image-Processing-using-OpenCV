# image manupulation using Draw linw, cercle, rectangle, add text
# import opencv library
import cv2

# create a variable and store the image file link
image = cv2.imread(input("Enter the Image Link:- "))

#use Display the image on screen
cv2.imshow(("Image"), image)

#display the image until any key press from the keyboard
cv2.waitKey(0)

# off all others windows
cv2.destroyAllWindows()
print("Image Display Successfully...!")

# use .shpae method to check image dimension(height, Width, color)
h, w, c = image.shape
print("\nImage Dimension is :- "f" \nHeight:{h}\nWidth:{w}\nChannel:{c}")

#show option
print("\nChoose The Option:- ")
print("1.Draw Line on the Image ")
print("2.Draw Circle On the Image ")
print("3.Draw Rectangle on the image ")
print("4.Add Text on the Image ")
print("5.Exit")

# choose the option between this 5 option
Choise = input("\nEnter the Option (1, 2, 3, 4, 5):- ")

# if choose 1 execute this portion
if Choise == '1':
    x1 = int(input("Enter x1 :- "))
    y1 = int(input("Enter y1 :- "))
    x2 = int(input("Enter x2 :- "))
    y2 = int(input("Enter y2 :- "))
    pt1 = (x1,y1)
    pt2 = (x2,y2)
    color = 230
    thikness = int(input("Enter the thikness:- "))
    cv2.line(image, pt1, pt2, color, thikness)
    cv2.imshow("Draw Line image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Line Draw Successfull...\n")

    # in the section show youn want to save or exit option
    print("Choose the option:- ")
    print("1. Save the image")
    print("2.Exit")
    Choise = input("Enter the Option:- 1. or 2:- ")
    if Choise == '1':
        save = input("Enter the File name(e,g hello.png):- ")
        cv2.imwrite(save, image)
        print("Draw Line image saved successfully...")
    else:
        Choise == '2'
        print("Quit Successfull")
    exit()
elif Choise == '3':

    # if choose 3 execute this portion
    x1 = int(input("Enter First Starting Pixel x1 :- "))
    y1 = int(input("Enter End Starting  y1:- "))
    x2 = int(input("Enter First Starting Pixelx2 :- "))
    y2 = int(input("Enter End Starting Pixely2 :- "))
    pt1 = (x1,y1) # start rectangle point from this pixel
    pt2 = (x2,y2) # end rectangle on this 
    color = 230
    thikness = int(input("Enter the thikness:- "))
    cv2.rectangle(image, pt1, pt2, color, thikness)
    cv2.imshow(" Rectangle Draw image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Rectangle Draw Successfull...\n")
    print("Choose the option:- ")
    print("1. Save the image")
    print("2.Exit")
    Choise = input("Enter the Option:- 1. or 2:- ")
    if Choise == '1':
        save = input("Enter the File name(e,g hello.png):- ")
        cv2.imwrite(save, image)
        print("Draw Rectangle image saved successfully...")
    else:
        Choise == '2'
        print("Quit Successfull")
    exit(1)
elif Choise == '2':

    # if choose 2 execuute this portion
    pt1 = int(input("Enter the x :- "))
    pt2 = int(input("Enter the y :- "))
    center = pt1, pt2
    radius = int(input("Enter the radius:- "))
    color = 255
    thikness = int(input("Enter the thikness :- "))
    cv2.circle(image, center, radius, color, thikness)
    cv2.imshow("Circle Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Circle Draw Successfull...\n")

    # after successfull draw circle in image 
    # again option show 1. save the circle draw image or exit from this
    print("Choose the option:- ")
    print("1. Save the image")
    print("2.Exit")

    # if chhose 1 then save image according to the file link
    Choise = input("Enter the Option:- 1. or 2:- ")
    if Choise == '1':
        save = input("Enter the File name(e,g hello.png):- ")
        cv2.imwrite(save, image)
        print("Circle Line image saved successfully...")

        # exit from this
    else:
        Choise == '2'
        print("Quit Successfull")
    exit()
elif Choise == '4':

    # if choose 4 execute this portion
    text = input("Enter the text:- ")
    pt1 = int(input("Enter Starting Pixel X values:- "))
    pt2 = int(input("Enter Ending Pixel Y value:- "))
    point = pt1, pt2
    color = 255
    font = int(input("Enter the Font Size:- "))
    thikness = int(input("Enter the thikness:- "))
    cv2.putText(image, text, point, cv2.FONT_HERSHEY_SIMPLEX,font, color, thikness)
    cv2.imshow("Text Add Image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Text Added Successfully...\n")
    print("Choose the option:- ")
    print("1. Save the image")
    print("2.Exit")
    Choise = input("Enter the Option:- 1. or 2:- ")
    if Choise == '1':
        save = input("Enter the File name(e,g hello.png):- ")
        cv2.imwrite(save, image)
        print("Text Added image saved successfully...")
    else:
        Choise == '2'
        print("Quit Successfull")
    exit()
else:
    Choise == '5'
    print("Exit Successfull...\n")