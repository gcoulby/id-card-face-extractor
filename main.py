import cv2
import os
import argparse

# Global variables
input_dir = ''
output_dir = ''
show_windows = False
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def get_face_from_image(fileName):  
    """
    Gets the face from an image and saves it in the output directory
    Parameters
    ----------
    fileName : str
        The name of the file to get the face from
    """

    # Read the image
    image = cv2.imread(f'{input_dir}/{fileName}')

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if show_windows:
        # show the original image in a window
        cv2.imshow('Original image', image)

    # Detect the faces
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    # check if faces are detected
    if len(faces) == 0:
        print("No faces found")

    # Draw rectangles around the faces, crop the image and save it
    for (x, y, w, h) in faces:
        x = x - 25 # Padding trick to take the whole face not just Haarcascades points
        y = y - 40 # Same here...
        cv2.rectangle(image, (x, y), (x + w + 50, y + h + 70), (27, 200, 10), 2)
        #crop the image frame into rectangle
        roi_color = image[y:y + h + 70, x:x + w + 50]
        print("[INFO] Object found. Saving locally.")
        
        # Save the cropped image
        cv2.imwrite(f'{output_dir}/{fileName[0:fileName.rfind(".")]}_face.jpg', roi_color)

        if show_windows:
            # uncomment to show the detected face in a window and wait for a key press
            cv2.imshow('Face Detection', image)
            cv2.waitKey(0)

    # Destroy all windows
    cv2.destroyAllWindows()


def main():
    """
    The main function of the program
    """
    global input_dir, output_dir

    # Create the parser
    parser=argparse.ArgumentParser(description='Get faces from images of PhotoID cards', epilog='Enjoy the program! :)', )

    # Add the arguments to the parser
    parser.add_argument("-i", "--input", help="input directory")
    parser.add_argument("-o", "--output", help="output directory")

    # Parse the arguments
    args=parser.parse_args()
    if(args.input == None):
        # If no input directory is provided, exit the program
        print("Please provide input directory as first argument")
        exit(1)
    if(args.output == None):
        # If no output directory is provided, exit the program
        print("Please provide output directory as second argument")
        exit(1)

    # Set the input and output directories from the arguments passed 
    # to the script and remove trailing slashes if they exist
    input_dir = args.input.strip('/')
    output_dir = args.output.strip('/')

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    # Get all the files in the input directory
    fileNames = os.listdir(input_dir)
    for fileName in fileNames:
        # Get the face from each image
        get_face_from_image(fileName)


if __name__ == "__main__":
    main()