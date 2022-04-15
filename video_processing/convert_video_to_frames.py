import sys
import cv2
import os
import random
import string


def isint(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def random_string(length):
    """It generates a random string used to name the files while processing the video file"""
    stringname = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
                      for i in range(length))
    return stringname


def length_of_video(video_path):
    """Helper function"""
    cap = cv2.VideoCapture(video_path)
    if cap.isOpened():
        print("opened")
    else:
        print("not opened and error")
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    return length


def extracting_frames(video_path, save_path, skip_frames):
    if isint(skip_frames):
        """Extract frames using the video path into the save path every X value
        where X = skip_frames"""
        print("******************Starting extraction******************")
        _, filename = os.path.split(video_path)
        filename_without_extension = os.path.splitext(filename)[0]
        length = length_of_video(video_path)
        if length == 0:
            print("Error, length of the given path is 0. Exiting.")
            return 0

        cap = cv2.VideoCapture(video_path)

        count = 0
        randomstr = random_string(5)

        # ret checks if the frame was correctly picked up, frame stores the frame read.
        ret, frame = cap.read()
        testfile = os.path.join(save_path, filename_without_extension[:6] +
                                '{}_{}.jpg'.format(randomstr, count))
        cv2.imwrite(testfile, frame)
        if os.path.isfile(testfile):
            print("The test of the first frame was successful, continuing extraction")

            count = 1
            while ret:
                ret, frame = cap.read()
                if ret and count % int(skip_frames) == 0:
                    cv2.imwrite(os.path.join(save_path, filename_without_extension[:6] +
                                '{}_{}.jpg'.format(randomstr, count)), frame)
                    count += 1
                    print("Frame nr "+str(count))
                else:
                    count += 1
        else:
            print("Problems saving the file in cv2 encoding, cannot save the file")
            return 0

        cap.release()
        print("******************Finished extracting******************")
    else:
        print("Error the skip_frames parameter should be an integer. Exiting program...")
        sys.exit()


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Error, this application needs 3 parameters to run!")
        print("Usage: python3 convert_video_to_frames.py input_video output_directory frames_to_skip(for example 60).")
        sys.exit()

    if len(sys.argv[1]) and len(sys.argv[2]) and len(sys.argv[3]) > 0:
        inputfile = sys.argv[1]
        outputfolder = sys.argv[2]
        framestoskip = sys.argv[3]

        print("i: " + inputfile + ". o: " + outputfolder + ". fts: " + framestoskip)
        extracting_frames(inputfile, outputfolder, framestoskip)
    else:
        print("Error, one or more given parameters has no length! Exiting")