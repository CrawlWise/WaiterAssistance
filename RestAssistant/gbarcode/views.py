from django.shortcuts import render
import segno
import os

# Create my qr code here:
# generate my barcode image
def qrGenerator():
    generate_qrcode = segno.make_qr("https://www.takemenowhere.com")
    save_qrcode = generate_qrcode.save("customerRequest.png", scale=15, border=0)
    return save_qrcode

# Create your views here.
def generateBarcode(request):
    # Get the current working dir
    initial_dir = os.getcwd() # Get current directory
    pushdir = initial_dir + "\\gbarcode\\static\\img" # Append current directory with the gbarcode directory
    # basefile = os.path.basename(pushdir + "\\customerRequest.png")
    chdir = os.chdir(pushdir)
    qrGenerator()
    os.chdir(initial_dir)
    return render(request, 'gbarcode.html')
