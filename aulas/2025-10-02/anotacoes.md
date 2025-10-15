# Estruturas de repetição

Tipos: pré-teste ou incondicional.  

Em uma estrutura de repetição, as variáveis podem ser _acumuladoras_ ou _contadoras_. Acumuladoras acumulam valores (concatenação, soma de valores, ...). Contadoras contam e controlam a execução das repetições.

## while

```
while <condicao>:
    <instrucao>
```
## for

```
for <nome_variavel> in <iteravel>:
    <instrucoes>
```

Sendo `<iteravel>` uma lista, tupla, string, um dicionário...

Exemplo:
```
cont = 0
soma = 0

for n in range(0, 850): # 0...849
    # ...
```

Formatos para `range`:
- `range(10)`
- `range(1, 10)`
- `range(0, 10, 2)`
- `range(0, -10, -1)`

# Controlando a execução do loop

Podem ser usados `break` e `continue`.
