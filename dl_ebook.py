import argparse
import os
import pyautogui as pag
import datetime
import time
import shutil
import img2pdf
from PIL import Image

dt_now = datetime.datetime.now()

parser = argparse.ArgumentParser()
parser.add_argument('page_num', type=int, help='Total number of pages')
parser.add_argument('-r', '--region', type=str,
                    default='580,0,1340,1080', help='x1,y1,x2,y2')
parser.add_argument('-p', '--pdf', action='store_true', help='Output as pdf')
parser.add_argument('-d', '--delete-image',
                    action='store_true', help='Delete image files')
parser.add_argument('-o', '--output-file-name', type=str,
                    default=dt_now.strftime('%Y_%m%d_%H%M%S'), help='Name of the file to output')
parser.add_argument('-l', '--left-scroll',
                    action='store_true', help='Scroll direction left')
parser.add_argument('-v', '--interval-time', type=float,
                    default=10, help='Interval time before starting the screenshot[s].')
args = parser.parse_args()

PAGE_NUM = args.page_num
REGION = tuple(map(int, args.region.split(',')))
PDF = args.pdf
DELETE_IMG = args.delete_image
FILE_NAME = args.output_file_name
INTERVAL_TIME = args.interval_time
if args.left_scroll:
    SCROLL_DIRECTION = 'left'
else:
    SCROLL_DIRECTION = 'right'


def screenshot():
    if not os.path.exists(fr'outputs/{FILE_NAME}'):
        os.makedirs(fr'outputs/{FILE_NAME}')
    for page in range(PAGE_NUM):
        x1, y1, x2, y2 = REGION
        sc = pag.screenshot(region=(x1, y1, x2-x1, y2-y1))
        sc.save(fr'outputs/{FILE_NAME}/{page+1}.png')
        pag.press(SCROLL_DIRECTION)
        time.sleep(0.5)


def img_to_pdf():
    pdf_FileName = fr'outputs/{FILE_NAME}.pdf'
    img_folder = fr'outputs/{FILE_NAME}/'
    extension = '.png'

    with open(pdf_FileName, 'wb') as f:
        f.write(img2pdf.convert([Image.open(
            img_folder+j).filename for j in os.listdir(img_folder)if j.endswith(extension)]))


def delete_img():
    shutil.rmtree(fr'outputs/{FILE_NAME}/')


def main():
    time.sleep(INTERVAL_TIME)
    screenshot()
    if PDF:
        img_to_pdf()
        if DELETE_IMG:
            delete_img()


if __name__ == '__main__':
    main()
