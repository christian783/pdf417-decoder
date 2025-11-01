from pdf417decoder import PDF417Decoder

decoder = PDF417Decoder("C:\Users\Christian\OneDrive\Pictures\Screenshots\Screenshot-2025-11-01-205339.png")

for barcode in decoder.barcode_array:
    text = ''.join([chr(b) if 32 <= b <= 126 else ' ' for b in barcode.data])
    print(text.strip())
