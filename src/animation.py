import cv2
import numpy as np
from bicycle import Bicycle
from line import Line
from utils import draw_polygon, draw_line

FPS = 60
FRAME_TIME = 1 / FPS
VIDEO_OUTPUT = "../output/bicycle_simulation.mp4"

def animate(bicycle, line, duration):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(VIDEO_OUTPUT, fourcc, FPS, (800, 600))

    for _ in np.arange(0, duration, FRAME_TIME):
        frame = np.zeros((600, 800, 3), dtype=np.uint8)

        for wheel in bicycle.wheels:
            draw_polygon(frame, wheel.polygon, (0, 255, 0))

        draw_line(frame, line, (255, 0, 0))

        bicycle.move(FRAME_TIME)
        video.write(frame)

    video.release()