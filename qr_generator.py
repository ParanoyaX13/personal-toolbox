try:
    import qrcode
except ImportError:
    print("qrcode library not installed. Install with: pip install qrcode[pil]")
    exit()

def qr_code_generator():
    """Generate QR Code from text or URL"""
    print("\n=== QR Code Generator ===")
    data = input("Enter text or URL to generate QR code: ").strip()
    
    if not data:
        print("No input provided.")
        return
    
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    filename = f"qr_{data[:10].replace(' ', '_')}.png"
    img.save(filename)
    print(f"✅ QR Code saved as: {filename}")
    print("You can open the image in your file manager.")

if __name__ == "__main__":
    qr_code_generator()
