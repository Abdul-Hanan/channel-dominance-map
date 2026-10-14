# channel-dominance-map

Visualizes per-pixel dominant BGR channels in a static color image.

## What it Does

This project generates a "dominant channel map" from a given static color image. For each pixel in the original image, it determines whether its Blue, Green, or Red channel has the highest intensity. Based on this, it then sets the corresponding pixel in the generated map to be purely blue, green, or red, respectively. In cases of a tie in intensity (e.g., yellow = green + red), the channel with the lowest BGR index (Blue, then Green, then Red) is chosen as dominant. The original image and the generated map are then saved side-by-side into a single output image file.

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/channel-dominance-map.git
    cd channel-dominance-map
    ```
    (Note: Replace `https://github.com/your-username/channel-dominance-map.git` with the actual repo URL if this were a real project.)

2.  **Install dependencies:**
    It's recommended to use a virtual environment.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3.  **Run the script:**
    ```bash
    python main.py
    ```

## Output

The script will generate an image file named `dominant_channel_map_output.png` in the same directory where `main.py` is executed. This file will contain the synthetic input image on the left and its corresponding dominant channel map on the right. No GUI windows will be displayed during execution, making it suitable for headless environments.