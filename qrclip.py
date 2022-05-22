#!/usr/bin/env python3

## START imports region
from qrcode import QRCode, ERROR_CORRECT_L    # QRCode is QR code generator class and ERROR_CORRECT_L is error level
from pyperclip import paste                   # paste() is function to get current clipboard buffer
## END imports region

## START functions region
# This function generates QR code from `text` argument passed and outputs it on terminal screen
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
    # Add text to the QR code
    qr.add_data(text)
    # Compile the QR code
    qr.make(fit = True)
    # Output to terminal
    qr.print_tty()
    
# Function for passing clipboard content to print_qr_code()
def main() -> None:
    """Main function"""

    clipboard_buffer: str = paste()
    print_qr_code(clipboard_buffer)
## END functions region

## START main region
if __name__ == "__main__":    # if we are running script as "python qrclip.py" then it executes this code
    main()
## END main region
