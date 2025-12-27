from fpdf import FPDF

pdf = FPDF('P', 'mm', 'A4')

pdf.add_page()
pdf.set_font('Arial', '', 16) #Familia, estilo (normal, B negrito, I itálico, U sublinhado), tamanho
pdf.cell(60, 20, 'Curso de Python', 1, 1, 'C') # largura, altura, texto, borda, quebra de página
pdf.set_font('Times', 'B', 20) #Familia, estilo (normal, B negrito, I itálico, U sublinhado), tamanho
pdf.cell(60, 20, 'Curso de Python', 1, 1, 'L') # largura, altura, texto, borda, quebra de página
pdf.set_font('Times', 'I', 16) #Familia, estilo (normal, B negrito, I itálico, U sublinhado), tamanho
pdf.cell(60, 20, 'Curso de Python', 1, 1, 'R') # largura, altura, texto, borda, quebra de página
pdf.add_page('L')
pdf.add_page()

pdf.output('pdf/exemplo.pdf', 'f')