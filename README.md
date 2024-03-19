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
- Open-CV library

if you are unfamiliar with Python, PyCharm can be used to download the opencv-python library from its built-in package management.

## Usage
- run the Python Script
- Select the desired image for the folder icon
- Adjust the position of the image using the trackbar (alternatively, cv2.resize can be used to stretch the image to fit the icon)
- Press q
- It should be done!

## Extra Note
To use another image for the icon, simply run the script again as it will override it.

To restore defaults, go to the Customize tab under the folder's properties.

To modify the desktop.ini or icon.ico, use the command ```attrib -s -h "C:\Users\path\to\the\folder\desktop.ini" ``` in your Windows cmd.
