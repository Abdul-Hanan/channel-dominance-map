import cv2
import numpy as np

def create_synthetic_image(width=300, height=300):
    """
    Creates a synthetic image with distinct Red, Green, Blue, and mixed regions
    to demonstrate channel dominance.
    """
    img = np.zeros((height, width, 3), dtype=np.uint8)

    # Top-left quadrant: Pure Red (BGR: 0, 0, 255)
    img[0:height//2, 0:width//2] = [0, 0, 255]
    
    # Top-right quadrant: Pure Green (BGR: 0, 255, 0)
    img[0:height//2, width//2:width] = [0, 255, 0]
    
    # Bottom-left quadrant: Pure Blue (BGR: 255, 0, 0)
    img[height//2:height, 0:width//2] = [255, 0, 0]
    
    # Bottom-right quadrant: Yellow (BGR: 0, 255, 255)
    # np.argmax will pick Green (index 1) in case of a tie with Red (index 2)
    # because G appears earlier in the BGR order.
    img[height//2:height, width//2:width] = [0, 255, 255]

    # Add a thin strip of cyan (B=255, G=255, R=0) to show blue dominance tie-breaking
    # np.argmax will pick Blue (index 0) in case of a tie with Green (index 1)
    img[height//2-10:height//2+10, width//4:width*3//4] = [255, 255, 0]

    return img

def generate_dominant_channel_map(image):
    """
    Generates a map where each pixel is colored purely Red, Green, or Blue
    based on which of its BGR channels had the highest intensity in the
    original image. In case of ties, the channel with the lowest BGR index
    (Blue then Green then Red) is chosen.
    """
    # Create an empty black image of the same dimensions and type as the input
    dominant_map = np.zeros_like(image)

    # Find the index of the maximum intensity channel for each pixel.
    # BGR order: 0 for Blue, 1 for Green, 2 for Red.
    # np.argmax handles ties by returning the first occurrence of the maximum.
    dominant_indices = np.argmax(image, axis=2)

    # Use advanced indexing to efficiently set the dominant channel to 255.
    # `rows` and `cols` provide the (y, x) coordinates for each pixel.
    rows, cols = np.indices(dominant_indices.shape)
    
    # For each pixel at (row, col), set the channel specified by dominant_indices[row, col] to 255.
    dominant_map[rows, cols, dominant_indices] = 255

    return dominant_map

def main():
    print("Starting dominant channel map generation process...")

    # 1. Generate a synthetic input image
    print("Generating synthetic input image...")
    original_image = create_synthetic_image(width=400, height=300)

    # 2. Generate the dominant channel map from the original image
    print("Generating dominant channel map...")
    dominant_map = generate_dominant_channel_map(original_image)

    # 3. Combine the original image and the generated map side-by-side
    print("Combining original image and map side-by-side...")
    combined_output = np.hstack((original_image, dominant_map))

    # 4. Save the combined output image to a file
    output_filename = "dominant_channel_map_output.png"
    cv2.imwrite(output_filename, combined_output)
    
    print(f"Process complete. Output saved to '{output_filename}'")
    print("Remember to open 'dominant_channel_map_output.png' to view the result.")

if __name__ == "__main__":
    main()