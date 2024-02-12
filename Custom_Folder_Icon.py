import cv2
import os
from tkinter.filedialog import askopenfilename


def main():
    file_path = askopenfilename(initialdir=os.curdir)
    folder_path = os.path.dirname(file_path)

    parameter1 = f'temp_img.jpg'
    parameter2 = f'{folder_path}/icon.ico'

    # get a square image for icon
    img = square(file_path)
    cv2.imwrite(parameter1, img)

    # write and store icon
    if os.path.isfile(parameter2):
        os.remove(parameter2)
    os.system(f'convert "{parameter1}" -define icon:auto-resize=16,48,256 -compress zip "{parameter2}"')
    os.remove(parameter1)

    # change folder icon
    change_folder_icon(folder_path, parameter2)
    return


def square(path):
    img = cv2.imread(path)
    row, col, chn = img.shape

    # if the image is square, return
    if row == col:
        return img

    # find the smaller dimension value and set it as the resolution
    res = min(row, col)
    end = abs(row-col)

    # trackbar for position adjustment
    winname = 'Cropped Image [press q to continue]'
    cv2.namedWindow(winname)
    cv2.createTrackbar('Position', winname, 0, end, k)

    while True:
        # get desired position
        pos = cv2.getTrackbarPos('Position', winname)

        # crop position based on pos input
        if row > col:
            img_cropped = img[pos:res+pos, 0:res]
        else:
            img_cropped = img[0:res, pos:res+pos]

        # show cropped image
        cv2.imshow(winname, img_cropped)

        # end loop
        if cv2.waitKey(100) == ord('q'):
            cv2.destroyAllWindows()
            break
    return img_cropped


def k(x):
    pass


def change_folder_icon(folder_path, icon_path):
    # Create or update the desktop.ini file
    ini_path = os.path.join(folder_path, 'desktop.ini')

    # clear previous .ini file
    if os.path.isfile(ini_path):
        os.remove(ini_path)

    # apply new icon to folder
    with open(ini_path, 'w') as f:
        f.write('[.ShellClassInfo]\r\n')
        f.write(f'IconResource={icon_path}\r\n')
        f.write(f'IconFile={icon_path}\r\n')
        f.write('IconIndex=0\r\n')
        f.write('ConfirmFileOp=0\r\n')
        f.write('[ViewState]\r\n')
        f.write('FolderType=Pictures\r\n')
    f.close()

    # set folder to read
    os.system(f'attrib +r "{folder_path}"')

    # hide icon and ini file
    os.system(f'attrib +s +h "{icon_path}"')
    os.system(f'attrib +s +h "{ini_path}"')
    return


if __name__ == '__main__':
    main()
