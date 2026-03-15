import cv2
import numpy as np
from src.config import BLUE_LOWER, BLUE_UPPER, TORSO_VERTICAL_RATIO, TORSO_HORIZONTAL_RATIO

def extract_torso(player_img):
    h, w, _ = player_img.shape
    v_start = int(h * TORSO_VERTICAL_RATIO[0])
    v_end = int(h * TORSO_VERTICAL_RATIO[1])
    h_start = int(w * TORSO_HORIZONTAL_RATIO[0])
    h_end = int(w * TORSO_HORIZONTAL_RATIO[1])
    return player_img[v_start:v_end, h_start:h_end]

def detect_blue_ratio(torso_img):
    hsv = cv2.cvtColor(torso_img, cv2.COLOR_BGR2HSV)
    lower_blue = np.array(BLUE_LOWER)
    upper_blue = np.array(BLUE_UPPER)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    return np.sum(mask > 0) / (torso_img.shape[0] * torso_img.shape[1])
