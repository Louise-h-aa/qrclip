#!/usr/bin/env python3
import qrcode
import pyperclip

#Function for printing qrcode to terminal
def print_qr_code(text):
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.ERROR_CORRECT_L,
                       box_size=10,
                       border=4)
   
    #Add text to the qrode
    qr.add_data(text)
    
    #Compile the qrcode
    qr.make()

    #To terminal
    qr.print_tty()
    

#Function for generating the paste output 
def main ():
    clipboard_content = pyperclip.paste()
    print_qr_code(clipboard_content)   
    

if __name__ == "__main__":
    main()
    
