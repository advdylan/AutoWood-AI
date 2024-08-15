from reportlab.pdfgen import canvas
import os
import requests

x = 595.27
y = 841.89



def get_data(id):
    try:
        response = requests.get(f'http://127.0.0.1:8000/api/v1/newproject/{id}')
        project_data = response.json()
        return project_data
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

def footer(c):
    c.line(0, 35, 595.27, 35) #footer line size
    c.drawCentredString(x/2, 35/2, "| Auto - Wood |")

def header(c, project_name):
    c.setFont("Times-Italic", 18)
    c.line(0, y - 35, 595.27, y-35)  
    c.drawCentredString(x/2, y-(35/2)-5, f"Wycena zamówienia: {project_name}")

project_data = get_data(53)
project_name = project_data["name"]


c = canvas.Canvas("hello.pdf")

footer(c)
header(c, project_name)
c.showPage()
c.save()

