## 📚 2. Documentación

---

### 🔍 2.1 Definición del lenguaje

> **🛠️ Elementos Léxicos**
>
> * **Comentarios de línea**: `//…` hasta fin de línea.
> * **Palabras reservadas (keywords)**:
>
>   * Control: `main`, `for`, `while`, `if`
>   * Tipos: `number`, `string`, `Boolean`
>   * Literales booleanas: `True`, `False`
>   * Funciones built-in: `echo`, `input`
> * **Identificadores**:
>
>   * Formato: `[A-Za-z][A-Za-z0-9]*`
>   * Ejemplos válidos: `foo`, `bar2`, `X123`
>   * No válidos: `_privado`, `9inicio`
> * **Números**:
>
>   * 🔢 **Enteros**: `1`, `42`, `123`
>   * 🌊 **Flotantes**: `1.2`, `.2`, `.231`
> * **Cadenas**: delimitadas por `"…"` o `'…'`, con escapes `\"` y `\'`.
> * **Operadores**:
>
>   * Aritmética: `+`, `-`, `*`, `/`, `++`, `--`, `!`
>   * Comparación: `=`, `==`, `!=`, `<`, `>`, `<=`, `>=`
> * **Delimitadores y agrupadores**: `{ }`, `( )`, `,`, `;`

---

### 🏗️ 2.2 Estructura de los programas aceptados

```c
main ProgramaEjemplo() {
    // Sentencias…
}
```

1. **Programa Principal**:

   * Debe iniciar con `main <identificador>() { … }`.
2. **Bloques**:

   * Agrupados por `{ … }`.
3. **Sentencias**:

   * Terminan con `;` (excepto cabeceras de `for`, `while`, `if`).
4. **For Loop**:

   ```c
   for ( init , cond , step ) {
     …
   }
   ```

   * Componentes separados por comas.
5. **While Loop**:

   ```c
   while ( cond ) { … }
   ```
6. **Condicional**:

   ```c
   if ( cond ) { … }
   ```

---

### 📝 2.3 Instrucciones y Sintaxis

| 🔖 Instrucción | 📐 Sintaxis                     | 📖 Descripción                              |
| -------------- | ------------------------------- | ------------------------------------------- |
| Declaración    | `number id = expr;`             | Declara e inicializa variable numérica.     |
|                | `string id = expr;`             | Declara e inicializa variable de texto.     |
|                | `Boolean id = expr;`            | Declara e inicializa variable booleana.     |
| Asignación     | `id = expr;`                    | Asigna valor a variable existente.          |
| Entrada        | `string id = input("mensaje");` | Lee texto de consola.                       |
| Salida         | `echo("mensaje");`              | Imprime en consola.                         |
| For Loop       | `for (init, cond, step) { … }`  | Bucle con inicialización, condición y paso. |
| While Loop     | `while (cond) { … }`            | Bucle condicionado.                         |
| Condicional    | `if (cond) { … }`               | Ejecuta bloque si `cond` es verdadera.      |
| Comentario     | `// comentario`                 | Ignorado por el lexer.                      |

---
