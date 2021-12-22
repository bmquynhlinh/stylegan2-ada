import os
import cv2

def load_image(root_dir):
    list_file = []
    for (dir_path, dir_names, filenames) in os.walk(root_dir):
        list_file += [os.path.join(dir_path, file) for file in filenames]
    for file in list_file:
        img = cv2.imread(file)
        img2 = cv2.resize(img, (256,256))
        cv2.imwrite(file,img2)
    return None
def main():
    load_image('./database/cartoonset10k/cartoonset10k')

if __name__ =='__main__':
    main()