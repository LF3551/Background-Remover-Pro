# Background Remover Pro 🚀

Easily remove backgrounds from images using Python! This project leverages the power of the `rembg` library to make background removal as simple as a few lines of code.

### Features
- 🌟 **Quick and Easy**: Minimal setup and lightning-fast background removal.
- 🖼️ **High Quality**: Preserve the quality of your images while removing backgrounds.
- 🛠️ **Customizable**: Extend the script to fit your needs.

### How It Works
Provide an input image, and the script will output the same image with its background removed. Perfect for product photography, graphic design, and more.

### Example:
Before (Input Image):
![Input Image](input.jpg)

After (Output Image):
![Output Image](output.png)


---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/LF3551/Background-Remover-Pro.git
   cd background-remover-pro
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Downloading Pre-trained Model (If Missing): When you run the script for the first time, it will automatically download the necessary pre-trained model (u2net.onnx). If the model is not downloaded, you can manually download it from here and place it in the directory:
   ```bash
~/.u2net/
   ```

## Usage

1. Prepare your input image:
   - Place your image (e.g., `input.jpg`) in the project folder

2. Run the script:
   ```bash
   python3 main.py input.jpg output.png
   ```

3. Output:
   - The script will save the processed image as `output.png` in the same folder
   - The console will confirm the save location:
   ```
   Background removed! Saved as output.png
   ```


## License
This project is open-sourced under the Universal Permissive License (UPL), Version 1.0. See the LICENSE file for more details.