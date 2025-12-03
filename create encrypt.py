from PIL import Image

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)  # XOR again restores original

    img.save(output_path)
    print("Image decrypted successfully:", output_path)


input_img = input("Enter encrypted image path: ")
output_img = input("Enter output decrypted image name: ")
key = int(input("Enter the same encryption key: "))

decrypt_image(input_img, output_img, key)
