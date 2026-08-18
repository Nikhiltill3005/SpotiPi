
#!/usr/bin/env python
import time
import sys
import os.path

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

def display_gif(matrix):
    gif = Image.open("default.gif")
    num_frames = gif.n_frames

    # Preprocess the gifs frames into canvases to improve playback performance
    frames = []
    canvas = matrix.CreateFrameCanvas()
    print("Preprocessing gif, this may take a moment depending on the size of the gif...")
    for frame_index in range(0, num_frames):
        gif.seek(frame_index)
    # must copy the frame out of the gif, since thumbnail() modifies the image in-place
        frame = gif.copy()
        frame.thumbnail((matrix.width, matrix.height), Image.LANCZOS)
        frames.append(frame.convert("RGB"))

    # Close the gif file to save memory now that we have copied out all of the frames
    gif.close()

    try:
        print("Press CTRL-C to stop.")

        # Infinitely loop through the gif
        cur_frame = 0
        while(True):
            canvas.SetImage(frames[cur_frame])
            matrix.SwapOnVSync(canvas, framerate_fraction=10)
            if cur_frame == num_frames - 1:
                cur_frame = 0
            else:
                cur_frame += 1
    except KeyboardInterrupt:
        sys.exit(0)

def display_image(input_matrix,image):
    img = Image.open(image)
    img.thumbnail((input_matrix.width,input_matrix.height),Image.LANCZOS)
    input_matrix.SetImage(img.convert('RGB'))

def configure_matrix():
    options = RGBMatrixOptions()
    options.rows = 64
    options.cols = 64
    options.chain_length = 1
    options.parallel = 1
    options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
    matrix = RGBMatrix(options = options)

    return matrix

def check_file():
    cover_art_flag = os.path.isfile("album.jpg")
   # print("RUNNING FUNCTION")
   # print(cover_art_flag)
    return cover_art_flag

def main():
    cover_art_flag = check_file()
    #print("Running Main")
    matrix = configure_matrix()
    while True:
        #print("running while")
        if cover_art_flag == True:
             display_image(matrix,"album.jpg")
             cover_art_flag = check_file()
             #print("Running album image")

        elif cover_art_flag == False:
             #print("Default Image SHOWING")
             display_image(matrix,"default.jpg")
             cover_art_flag = check_file()
             #print("Running default image")



main()

