from fpdf import FPDF

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.image('pdf/logo.png', 70, 120)
pdf.image('pdf/logo.png', 90, 200, 20, 20)
pdf.output('pdf/files/imagem.pdf', 'F')