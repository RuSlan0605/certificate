from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab import platypus


from PIL import Image, ImageDraw, ImageFont
from .models import Student

#reportlab
def generate_pdf(request):

    student = Student.objects.get(id=2)
    image = Image.open(student.certificate.path)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="certificate.pdf"'
    
    pdf = canvas.Canvas(response, pagesize=letter)

    width, height = letter
    image_width, image_height = image.size
    aspect_ratio = image_width / float(image_height)
    image_width = width - 80
    image_height = image_width / aspect_ratio   
    
    pdf.drawImage(ImageReader(image), 40, 400, width=image_width, height=image_height)

    pdf.showPage()
    pdf.save()

    return response


def imgpack(request):

    students = Student.objects.all()

    for student in students:

        img = Image.open(student.certificate.path)
        font = ImageFont.truetype("fonts/majestic-x.ttf", size=155)
        idraw = ImageDraw.Draw(img)
        idraw.text((1225, 800), student.full_name, font=font)
        idraw.text((390, 1530), student.mentor, font=ImageFont.truetype('arial.ttf', size=70))
        idraw.text((2700, 1530), '21.09.2023', font=ImageFont.truetype('arial.ttf', size=70))
        idraw.text((678, 1150), student.course, font=ImageFont.truetype('arial.ttf', size=80))
        img.save(student.certificate.path)
        img = Image.open('bg.png')

        img.show()

    return img

