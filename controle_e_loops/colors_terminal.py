'''
   Estilo:
   0 - nenhum
   1 - Negriito
   2 - Sublinhado
   3 - Inverter

   Texto:
   30 - Branco
   31 - Vermelho
   32 - Verde
   33 - Amarelo
   34 - Azul
   35 - Magenta
   36 - Ciano
   37 - Cinza

   Fundo:
   107 - Branco
   41 - Vermelho
   42 - Verde
   43 - Amarelo
   44 - Azul
   45 - Magenta
   46 - Ciano
   47 - Cinza

   \33[m]
   \033[estiilo; texto; fundom]
'''
print('\33[31mTeste de cor\33[0m')
print('\33[0;37mTeste de cor\33[m')

