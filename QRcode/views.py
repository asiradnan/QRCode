import qrcode
from django.shortcuts import render
import io
import base64


def qr(request):
    data=request.POST.get("data")
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(request.POST.get("data"))
    qr.make(fit=True)
    size = int(request.POST.get("size"))
    current_size = (4*qr.version+17)*qr.box_size
    while(current_size<size):
        qr.box_size+=1
        current_size = (4*qr.version+17)*qr.box_size
    img = qr.make_image(back_color=request.POST.get('backcolor'), fill_color=request.POST.get("color"))
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return render(request, 'qr.html', {'img': img_base64})

def home(request):
    return render(request, 'home.html')
