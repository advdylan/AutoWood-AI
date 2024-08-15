from reportlab.pdfgen import canvas

def customer_report(c):
    c.drawString(0,0, "Hello World dupa2")

c = canvas.Canvas("hello.pdf")
customer_report(c)
c.showPage()
c.save()

