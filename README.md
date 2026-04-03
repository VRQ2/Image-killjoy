# Image Degrader

A Python script that applies random degradation effects to images in a directory. This tool is designed to expand datasets for the `OpticalWasteSortingSystem`.

## Functionality

The script processes images from a source directory and saves the degraded versions to a destination directory:
1. **Command-Line Interface**: Accepts input and output directory paths as arguments.
2. **File Filtering**: Identifies files with `.png`, `.jpg`, or `.jpeg` extensions in the source directory.
3. **Randomized Processing**: For each image, it randomly applies one of the following effects:
   - **Contrast**: Randomly adjusted between 0.5 and 1.4.
   - **Gaussian Blur**: Applied with a random radius between 1.7 and 2.0.
   - **Solarize**: Applied with a random threshold between 180 and 240.
   - **Posterize**: Reduced to 1 or 2 bits.
4. **Saving**: Processed images are saved in the output directory using their original filenames.

## Requirements

- **Python 3.10+** (Uses the `match` statement).
- **Pillow**: For image processing.

### Installation
```bash
pip install Pillow
```

## Usage

Run the script by providing the path to the input directory and the desired output directory:

```bash
python3 image_compressor.py <input_directory> <output_directory>
```

### Arguments
- `input`: Path to the directory containing source images.
- `output`: Path to the directory where degraded images will be saved (created if it doesn't exist).
- `-c`, `--count`: Flag to indicate image count (feature implementation in progress).

## Example
```bash
python3 image_compressor.py ./start ./end
```
