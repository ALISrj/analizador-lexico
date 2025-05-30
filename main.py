# lexer_regex_keywords.py

import re
import sys

# 1) Lista de palabras reservadas
KEYWORDS = (
    "main", "number", "string", "Boolean", "True", "False",
    "for", "while", "if", "echo", "input", "and", "or"
)

# 2) Especificación de tokens (el orden importa)
token_specs = [
    # — keywords antes de ID, con \b para coincidir palabra completa
    ('RESERVADA',   rf'\b(?:{"|".join(KEYWORDS)})\b'),
    # — comentarios de línea
    ('COMENTARIO',   r'//[^\n]*'),
     # — operador incremental "++"
    ('INCREMENTO', r'\+\+'),
    ('DECREMENTO', r'--'),
    # — negación simple
    ('NEGACIÓN',       r'!'),
    # — cadenas entre comillas dobles o simples
    ('CADENA',    r'"[^"\n]*"'  r"|'[^'\n]*'"),
    # — flotantes: 123.456 | .456 | 456.
    ('DECIMAL',     r'\d+\.\d*|\.\d+'),
    # — enteros
    ('ENTERO',       r'\d+'),
    # — operadores compuestos
    ('OPERADOR_COMPUESTO', r'==|!=|<=|>='),
    # — operadores simples
    ('ASIGNACIÓN',      r'='),
    ('MENOR',     r'<'),
    ('MAYOR',     r'>'),
    ('SUMA',      r'\+'),
    ('RESTA',     r'-'),
    ('MULTIPLICACIÓN',      r'\*'),
    ('DIVISIÓN',       r'/'),
    # — agrupadores y puntuación
    ('LLAVE_IZQUIERDA',    r'\{'),
    ('LLAVE_DERECHA',    r'\}'),
    ('PARÉNTESIS_IZQUIERDO',    r'\('),
    ('PARÉNTESIS_DERECHO',    r'\)'),
    ('COMA',     r','),
    ('PUNTO_COMA',      r';'),
    # — identificadores: solo letras o dígitos, pero empezando por letra
    ('IDENTIFICADOR',        r'[A-Za-z][A-Za-z0-9]*'),
    # — espacios y tabulaciones (se ignoran)
    ('SKIP',      r'\s+'),
    # — cualquier otro símbolo no reconocido
    ('NO_RECONOCIDO',  r'.'),
]

# 3) Compilar el regex maestro
master_pat = re.compile(
    '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specs)
)

def analizar_texto(texto):
    for mo in master_pat.finditer(texto):
        tipo = mo.lastgroup
        valor = mo.group()

        # Ignora espacios y comentarios
        if tipo in ('SKIP', 'COMENTARIO'):
            continue

        # Ya no hace falta reasignar ID→KEYWORD, porque KEYWORD va antes

        if tipo == 'NO_RECONOCIDO':
            print(f"→ ERROR: símbolo inesperado {valor!r}")
        else:
            print(f"→ ÉXITO: {tipo:12} → {valor!r}")

def analizar_fichero(path):
    try:
        texto = open(path, encoding='utf-8').read()
    except FileNotFoundError:
        print(f"Error: no existe el fichero '{path}'")
        return
    print(f"Analizando '{path}':\n")
    analizar_texto(texto)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python lexer_regex_keywords.py <archivo_fuente.txt>")
    else:
        analizar_fichero(sys.argv[1])
