from io import BytesIO
import qrcode
from django.views.decorators.csrf import csrf_exempt
from .models import Contact
from django.http import HttpResponse
import qrcode.image.svg
from django.shortcuts import render, reverse
from django.contrib import messages
from django.core.files import File
from django.http import FileResponse


@csrf_exempt
def generate_vcard_qr(request):
    if request.method == 'POST':
        image = request.FILES.get('image', None)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        company = request.POST['company']
        title = request.POST['title']
        email = request.POST['email']
        company_address = request.POST['company_address']

        # Create the vCard data
        vcard_data = f"BEGIN:VCARD\nVERSION:3.0\nFN:{first_name} {last_name}\nORG:{company}\nTEL:{phone}\nEMAIL:{email}\nTITLE:{title}\nADR:{company_address}\nEND:VCARD"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=8,
            border=4,
        )
        qr.add_data(vcard_data)
        qr.make(fit=True)

        qr_img = qr.make_image(fill_color="black", back_color="white")
        response = HttpResponse(content_type="image/png")

        qr_img.save(response, "PNG")

        contact = Contact.objects.create(
            image=image,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            company=company,
            title=title,
            email=email,
            company_address=company_address,
        )

        # Save the QR code image as a file in the Contact model
        qr_img_io = BytesIO()
        qr_img.save(qr_img_io, format='PNG')
        contact.qr_code.save(f'{first_name}_{last_name}_qr.png', File(qr_img_io))

        return response

    return render(request, 'contacts/generate_vcard_qr.html')
