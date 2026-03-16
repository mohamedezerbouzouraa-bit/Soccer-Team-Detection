def detect_blue_ratio(torso_img):
    hsv = cv2.cvtColor(torso_img, cv2.COLOR_BGR2HSV)
    lower_blue = np.array(BLUE_LOWER)
    upper_blue = np.array(BLUE_UPPER)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    return np.sum(mask > 0) / (torso_img.shape[0] * torso_img.shape[1])
