
# SVG Optimizer

SVG Optimizer is a Python script designed to process HTML files and replace inline `data:image/svg+xml;base64` images with empty SVGs of the same dimensions. This optimization reduces the file size of your HTML documents, improving load times and overall performance.

## Features

- Extracts dimensions from existing SVG images.
- Replaces inline SVG images with empty SVGs while maintaining original dimensions.
- Simple file input and output for ease of use.

## Usage

1. **Clone the Repository**
   ```bash
   git clone https://github.com/pbrudny/svg-optimizer.git
   cd svg-optimizer
   ```

2. **Prepare Your HTML File**
   Place your input HTML file in the same directory as the script, or specify the path in the script.

3. **Run the Script**
   ```bash
   python replace_images.py
   ```

4. **Output**
   The script will generate an optimized HTML file named `updated_file.html` (or the name you specify in the script).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgments

Thank you for using SVG Optimizer! If you have any questions or feedback, feel free to open an issue on GitHub.
