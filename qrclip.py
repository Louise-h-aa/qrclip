#!/usr/bin/env python3
from qrcode import QRCode, ERROR_CORRECT_L
from pyperclip import paste

def print_qr_code(text: str) -> None:
    """
    Function for printing qrcode to terminal
    
    Arguments:
        text (str) : text to generate QR code from

    Returns: None
    """

    qr = QRCode(
        version = 1,
        error_correction = ERROR_CORRECT_L,
        box_size = 10,
        border = 4
    )
    # Add text to the qrode
    qr.add_data(text)
    # Compile the qrcode
    qr.make(fit = True)
    # To terminal
    qr.print_tty()
    

# Function for generating the paste output 
def main() -> None:
    """Main function"""

    print_qr_code(paste())   

if __name__ == "__main__":
    main()
    
