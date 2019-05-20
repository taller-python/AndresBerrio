print("Ingrese una palabra o frase: ")
palabra = input()
comparar = (palabra[::-1])
if palabra.replace(" ", "") == comparar.replace(" ", ""):
    print("Esta palabra o frase es palindroma")
else:
    print("Esta palabra o frase no es palindroma")