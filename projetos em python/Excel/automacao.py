import openpyxl 
from docxtpl import DocxTemplate
import datetime 

#excel

caminho = 'student_data.xlsx'
pasta_trabalho = openpyxl.load_workbook(caminho)
sheet = pasta_trabalho.active

lista_valores = list(sheet.values)
print(lista_valores)

#world

doc = DocxTemplate('certificate.docx')
for x in lista_valores[1:]:
    doc.render({
        'nome':x[0],
        'curso':x[1],
        'data':x[2].strftime('%d/%m/%Y'),
        'instrutor':x[3]
    })
    doc_nome = f'certificado {x[0]}.docx'
    doc.save(doc_nome)
