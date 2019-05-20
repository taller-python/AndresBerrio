import openpyxl, operator

ops = {"SUMA": operator.add,
       "RESTA": operator.sub,
       "MULTIPLICACIÓN": operator.mul,
       "DIVISIÓN": operator.floordiv}

print("escribe el nombre de la hoja de excel en mayscula y no olvides si tiene tilde")
operacion = input()
hojas = operacion
op_func = ops[operacion]

doc = openpyxl.load_workbook('C:/Users/andresberrio/Desktop/Python/operaciones.xlsx')
doc.sheetnames
hoja1 = doc[hojas]
i=1

with open('C:/Users/andresberrio/Desktop/Python/Archivo.txt', 'w') as file: 
    for fila in hoja1.rows:
        for columna in fila:
            if (i % 2) == 1:
                posanterior = columna.value
                i = i +1
            else:
                try:
                    if type(columna.value) is str and type(posanterior) is str:
                     file.write("error" + "\n")
                    else:
                     tipostring = op_func(columna.value, posanterior)
                     file.write(str(tipostring) + "\n")
                except:
                 file.write("error"+"\n")
                i = i + 1