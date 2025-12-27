from fpdf import FPDF

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.set_draw_color(255,100,100)
pdf.set_fill_color(255,100,100)
pdf.set_text_color(255,255,255)
pdf.cell(0, 20, 'Lista de Convidados', True, 1, 'C', True);

people = [
   ['Ana Braga', '(11)123456789', 2, 'A'],
   ['João Carlos', '(22)987654321', 2, 'B'],
   ['Clebar Cruz', '(33)147852369', 5, 'C'],
   ['Lucas Costa', '(44)963258741', 4, 'A'],
   ['Fernanda Gui', '(88)852147963', 2, 'C'],
]

pdf.set_font('courier', 'B', 12)
pdf.set_draw_color(100,100,100)
pdf.set_fill_color(100,100,100)
pdf.set_text_color(0,0,0)
subtitle = f'{"Nome":^35} {"Tel".center(20)} {"Acc".center(3)} {"Setor".center(5)}'
pdf.cell(0, 10, subtitle, False, 1, 'C', True)

pdf.set_font('courier', '', 12)

for i, person in enumerate(people):
   if (i%2 == 0):
      pdf.set_draw_color(200,200,200)
      pdf.set_fill_color(200,200,200)
      pdf.set_text_color(0,0,0)
      pdf.cell(0, 10, f'{person[0]:<35} {person[1]:<20}      {person[2]:^3} {person[3]:^5}', 0, 1, 'C', True)
      print('ok')
   else: 
      pdf.set_draw_color(255,255,255)
      pdf.set_fill_color(255,255,255)
      pdf.set_text_color(0,0,0)
      pdf.cell(0, 10, f'{person[0]:<35} {person[1]:<20}      {person[2]:^3} {person[3]:^5}', 0, 1, 'C', True)
      print('err')

pdf.output('pdf/convidados.pdf', 'f')