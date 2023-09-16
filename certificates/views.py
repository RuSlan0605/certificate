from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from reportlab.pdfgen import canvas
from reportlab import platypus
from PIL import Image, ImageDraw, ImageFont
from xhtml2pdf import pisa
from .models import Student

#reportlab
def generate_pdf(request):

    student = Student.objects.get(id=2)
    img_source = platypus.Image('/static/images/cert.jpg')

    #template = get_template('certificates/user_printer.html')
    '''context = {
        'student': student,
    }'''
    #html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="certificate.pdf"'
    
    pdf = canvas.Canvas(response)

    pdf.drawImage(img_source, 640, 480)

    pdf.showPage()
    pdf.save()

    return response


def render_pdf_view(request, pk):
    template_path = 'certificates/user_printer.html'
    students = get_object_or_404(Student, id=pk)
    context = {
        'students': students,
    }
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    
    template = get_template(template_path)
    html = template.render(context)


    # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def imgpack(request):

    student = Student.objects.get(id=2)
    full_name = student.full_name
    image = student.certificate
    date = student.date
    mentor = student.mentor
    course = student.course

    img = Image.open(image.path)
    font = ImageFont.truetype("fonts/majestic-x.ttf", size=155)
    idraw = ImageDraw.Draw(img)
    idraw.text((1225, 800), full_name, font=font)
    idraw.text((390, 1530), mentor, font=ImageFont.truetype('arial.ttf', size=70))
    idraw.text((2700, 1530), '06.09.2023', font=ImageFont.truetype('arial.ttf', size=70))
    idraw.text((678, 1150), course, font=ImageFont.truetype('arial.ttf', size=80))
    #idraw.text((300, 300), date,)
    img.save(image.path)
    img = Image.open('bg.png')

    img.show()

    return img

