# Windows-Custom-Icon
A Python script to implement a custom folder icon for your picture folders

Tired of seeing a half-opened picture folder icon blocking half of the image in File Explorer? Well, this script is just for you! This script will replace the half open picture folder icon with whatever image you selected. Just make sure the image is in the desired folder!

from this, ![image](https://github.com/AndyYeung1586/Windows-Custom-Icon/assets/101355842/50dbe2b6-40e9-4564-bafc-033e9ed58b4f) 
to this, ![image](https://github.com/AndyYeung1586/Windows-Custom-Icon/assets/101355842/f45d964e-7ce7-47ad-900f-a7bd74e75672)
and it works in all sizes from extra large, ![image](https://github.com/AndyYeung1586/Windows-Custom-Icon/assets/101355842/ad5aec0f-66d7-4166-9278-eb9eb7704f47)
 to small ![image](https://github.com/AndyYeung1586/Windows-Custom-Icon/assets/101355842/9cff3b2f-6957-4111-aa89-7ec89a4428dd).

I hope you find this script useful.

## Requirement
- Python 3.xx
- Open-CV

if you are unfamiliar with Python, I suggest you download PyCharm and download the opencv-python library from its built-in package management.

## Usage
- run the Python Script
- Select the image you want for the picture folder
- Adjust the position of the image using the trackbar on top (alternatively, you can use cv2.resize if you don't mind stretching the image)
- Press q
- It should be done!

## Extra Note
If you want to use another image for the icon, you can simply run the script again as it will override it. That said, it will take File Explorer an unspecified amount of time before it redates the icon. I would personally want to know why that is the case but oh well. 

If you want to restore defaults, go to the folder's properties. It is under the Customize tab.

If you want to modify desktop.ini or icon.ico for whatever reason, use the command ``` attrib -s -h "C:\Users\path\to\the\folder\desktop.ini" ``` in your windows cmd.
