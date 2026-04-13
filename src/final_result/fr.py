#number of players wearing blue jersey
print("Blue Team Players:", blue_count)
#number of players wearing white jersey
print("White Team Players:", white_count)
os.makedirs("outputs/annotated_images", exist_ok=True)
cv2.imwrite(f"outputs/annotated_images/{image_path}", img)
cv2_imshow(img)
