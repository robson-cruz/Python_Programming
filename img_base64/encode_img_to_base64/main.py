import base64


# Read the image file in binary mode
with open('logo.png', 'rb') as image_file:
    # Convert the binary data to base64 encoding
    base64_encoded_image = base64.b64encode(image_file.read())

# Convert the base64 encoded data to a string
base64_encoded_string = base64_encoded_image.decode('utf-8')

# Print or use the base64 encoded string
print(base64_encoded_string)
