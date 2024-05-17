import re
from base64 import b64decode, b64encode

def extract_svg_dimensions(svg_data):
    width = re.search(r'width="([\d.]+)px"', svg_data)
    height = re.search(r'height="([\d.]+)px"', svg_data)
    if width and height:
        return width.group(1), height.group(1)
    return None, None

def create_empty_svg(width, height):
    empty_svg = f'<svg width="{width}px" height="{height}px" xmlns="http://www.w3.org/2000/svg" version="1.1"></svg>'
    return b64encode(empty_svg.encode('utf-8')).decode('utf-8')

def replace_data_images(html_content):
    data_image_pattern = re.compile(r'src="data:image/svg\+xml;base64,([^"]+)"')
    matches = data_image_pattern.findall(html_content)
    
    for match in matches:
        svg_data = b64decode(match).decode('utf-8')
        width, height = extract_svg_dimensions(svg_data)
        if width and height:
            empty_svg_base64 = create_empty_svg(width, height)
            new_src = f'data:image/svg+xml;base64,{empty_svg_base64}'
            html_content = html_content.replace(f'data:image/svg+xml;base64,{match}', new_src)
    
    return html_content

# Read the HTML content from a file
input_file = 'input_file.html'  # Replace with your input file path
with open(input_file, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Process the HTML content
updated_html_content = replace_data_images(html_content)

# Save the updated HTML content to a new file
output_file = 'updated_file.html'  # Replace with your output file path
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(updated_html_content)

print("Data images replaced successfully!")
