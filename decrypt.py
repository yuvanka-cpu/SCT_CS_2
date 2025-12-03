from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)  # XOR encryption

    img.save(output_path)
    print("Image encrypted successfully:", output_path)


input_img = input("Enter input image path: ")
output_img = input("Enter output encrypted image name: ")
key = int(input("Enter encryption key (0-255): "))

encrypt_image(input_img, output_img, key)
