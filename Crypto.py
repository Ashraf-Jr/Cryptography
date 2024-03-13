# from PIL import Image 

# def gnerateData(data):
#     newData = []

#     for i in data :
#         # ba3mel convert le kol char 3han eb2a binary  
#         # append 3sahn a7otha feh newdata[] ba3d mah 3amltlha convert
#         newData.append(format(ord(i,'08b')))    
#         return newData   
    

# def modPix(pix , data) :
#     datalist = gnerateData(data)
#     lenghData = len(datalist)
#     imagedata = iter(pix)
#     # modify lel RBG 3shan el pixles 
#     #extracting 3 pixles 
#     for i in range(lenghData):
#         pix = [value  for value in imagedata.__next__()][:3] + imagedata.__next__[:3]+imagedata.__next__()[:3]

#         #pixles odd for 1 w even for 0 
#         for j in range(0, 8):
#             if (datalist[i][j] == '0') and (pix[j] % 2 != 0):
#                 pix[j] -= 1
#             elif (datalist[i][j] == '1') and (pix[j] % 2 == 0):
#                 if (pix[j] != 0):
#                     pix[j] -= 1
#                 else:
#                     pix[j] += 1


#     #The following nested loop then modifies the RGB values of each pixel based on the binary data. The LSB of each pixel value is replaced with the corresponding bit from the binary data.    
#     if (i== lenghData-1):
#         if(pix[-1]%2==0):
#             if(pix[-1]!=0):
#                 pix[-1]-=1
#             else:
#                 pix[-1]+=1
#     else:
#         if (pix[-1]%2 !=0):
#             pix[-1]-=1

#     #RGB tuple
#     pix = tuple(pix)
#     yield pix[0:3]# red
#     yield pix[3:6]# green   
#     yield pix[6:9]# blue

# def encode_encryption (newImage , data) :
#     width, height  = newImage.size[0], newImage.size[1]
#     (x,y) =(0,1)

#     for pixel in modPix(newImage.getpixel((x,y),data)):
#         newImage.putpixel((x,y), pixel)
#         if(x==width-1):
#             x=0
#             y+=1
#         else:
#             x+=1

# def encode():
#     img = input("Enter your  image name with extension : ")
#     # Open the image file specified by the user
#     image = Image.open(img,'r')

#     data = input('Enter the text you want to hide :')
#     if(len(data)==0):
#         raise ValueError('Data is empty')
    

#     newimg = image.copy()
#     encode_encryption(newimg,data)

#     new_img_name = input("Enter the name of the new image with extenstion:")

#     #Save the modified image under the specified filename
#     #Extract the image format (extension) from the filename
#     newimg.save(new_img_name , str(new_img_name.split(".")[1].upper()))



# def decode():
#     img = input("Enter your  image name with extension : ")
#     # Open the image file specified by the user
#     image = Image.open(img,'r')

#     data = " "
#     imgdata = iter(image.getdata())
#     while(True):
#         pixels = [value for value in imgdata.__next__()[:3]+ imgdata.__next__()[:3]+ imgdata.__next__()[:3]]

#         binaryString = " "

#         for i in pixels[:8]:
#             if(i%2 == 0 ):
#                 binaryString += '0'

#             else:
#                 binaryString += '1'



#         data += chr(int(binaryString,2))
#         if (pixels[-1]%2 !=0):
#             return data



# # Main Function 
#         def main():
#             a = int(input(":: welcome to Cryptpgraphy::\n"
#                               "1. Encode\n2. Decode\n"    ))  
#             if(a==1):
#                 encode()

#             elif(a==2):
#                 print("Decoded Message is : ",decode())
#             else :
#                 raise Exception("Enter correct choice")
#             # Driver code
#             if __name__=="__main__":
#                 main()

from PIL import Image 
import sys
print(sys.path)


def generateData(data):
    newData = []
    for i in data:
        # Convert each character to binary
        newData.append(format(ord(i), '08b'))
    return newData

def modPix(pix, data):
    datalist = generateData(data)
    lenghData = len(datalist)
    imagedata = iter(pix)
    
    for i in range(lenghData):
        pix = [value for value in imagedata.__next__()[:3] + imagedata.__next__()[:3] + imagedata.__next__()[:3]]

        # Modify the LSB of each pixel value based on binary data
        for j in range(0, 8):
            if (datalist[i][j] == '0') and (pix[j] % 2 != 0):
                pix[j] -= 1
            elif (datalist[i][j] == '1') and (pix[j] % 2 == 0):
                if (pix[j] != 0):
                    pix[j] -= 1
                else:
                    pix[j] += 1

        # Modify the last pixel value
        if (i == lenghData - 1):
            if (pix[-1] % 2 == 0):
                if (pix[-1] != 0):
                    pix[-1] -= 1
                else:
                    pix[-1] += 1
        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1

        pix = tuple(pix)
        yield pix[0:3]  # Red
        yield pix[3:6]  # Green   
        yield pix[6:9]  # Blue

def encode_encryption(newImage, data):
    width, height = newImage.size[0], newImage.size[1]
    (x, y) = (0, 1)

    for pixel in modPix(newImage.getpixel((x, y)), data):
        newImage.putpixel((x, y), pixel)
        if (x == width - 1):
            x = 0
            y += 1
        else:
            x += 1

def encode():
    img = input("Enter your image name with extension: ")
    # Open the image file specified by the user
    image = Image.open(img, 'r')

    data = input('Enter the text you want to hide: ')
    if (len(data) == 0):
        raise ValueError('Data is empty')

    newimg = image.copy()
    encode_encryption(newimg, data)

    new_img_name = input("Enter the name of the new image with extension: ")

    # Save the modified image under the specified filename
    # Extract the image format (extension) from the filename
    newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))

def decode():
    img = input("Enter your image name with extension: ")
    # Open the image file specified by the user
    image = Image.open(img, 'r')

    data = ""
    imgdata = iter(image.getdata())
    while True:
        pixels = [value for value in imgdata.__next__()[:3] + imgdata.__next__()[:3] + imgdata.__next__()[:3]]

        binaryString = ""

        for i in pixels[:8]:
            if (i % 2 == 0):
                binaryString += '0'
            else:
                binaryString += '1'

        data += chr(int(binaryString, 2))
        if (pixels[-1] % 2 != 0):
            return data

def main():
    a = int(input(":: welcome to Cryptography::\n1. Encode\n2. Decode\n"))
    if (a == 1):
        encode()
    elif (a == 2):
        print("Decoded Message is: ", decode())
    else:
        raise Exception("Enter correct choice")

if __name__ == "__main__":
    main()
