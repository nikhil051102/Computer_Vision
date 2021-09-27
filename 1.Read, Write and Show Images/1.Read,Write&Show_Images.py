import cv2

# Reading an Image : cv2.imread(filename, flag), Here if flag=1 then colored image,
# if flag=0 then Grayscale Image 
# if flag=-1 then Unchanged Image
img = cv2.imread('lena.jpg', 0)
print(img)

# Show image in particular windows : cv2.imshow(windowname, imagefilename)
cv2.imshow('image', img)


#To set time for window : cv2.waitKey(Time in Miliseconds)
#cv2.waitKey(0) : Window will be opened untill we close it manually.
k = cv2.waitKey(0)


#Closing/Destroying windows
# cv2.destroyAllWindows()


#Write an Image : 
# cv2.imwrite('filename in which u want to create with format like lena2.png', 'Image you want to copy')
# cv2.imwrite('1.Read, Write and Show Images/lena5.png', img)


#Saving an Image with Conditions
#Here, 27 is ASCII code of 'ESC' key.
#If we press 'Esc' key then image window will close without saving and if we press 's' then windows will be saved and closed.
if k == '27':               
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('lena2.png', img)
    cv2.destroyAllWindows()