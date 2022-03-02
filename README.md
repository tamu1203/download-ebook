# download-ebook
Convert kindle and other ebooks to png and pdf file by taking screenshots and merging it into a pdf.

# DEMO
https://user-images.githubusercontent.com/65435560/155957527-df1832fd-963e-40c8-a975-6f0f6f80e876.mp4

# Requirement
pyautogui

img2pdf
# Installation/Setup
```bash
pip install pyautogui
pip install img2pdf

git clone https://github.com/tamu1203/download-ebook.git
python dl_ebook.py page_num [-r REGION] [-p] [-d] [-o OUTPUT_FILE_NAME] [-l] [-i INTERVAL_TIME]
```
# Command line options
```bash
python dl_ebook.py page_num [-r REGION] [-p] [-d] [-o OUTPUT_FILE_NAME] [-l] [-i INTERVAL_TIME]
```
## -r --region
x1,y1,x2,y2 is window's coordinates

Default value: 580,0,1340,1080
## -p --pdf
Output as pdf

## -d --delete-image
Delete image files

## -o --output-fille-name
Name of the file to output

## -l --left-scroll
Scroll to the left

## -i --interval-time
Interval time before starting the screenshot.

Default value: 10

# License
[MIT license](https://en.wikipedia.org/wiki/MIT_License).
