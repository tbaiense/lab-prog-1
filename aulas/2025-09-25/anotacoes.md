# Funções novas

Novas funções mostradas:  

- `str.upper()`
- `str.lower()`

# Comandos

São as açõoes que realmente executadas. Não necessáriamente a quantidade exibida.

Exemplo:

```
print()

if true:
    print()
else:
    print()
```

# Desvio condicional

Tipos:
- simples
- composto
- aninhado
- seletivo

## Simples

Formato:  

```
if <condicao>: 
    instrucao1
```

Exemplo: 

```
idade = 18
if idade == 18:
    print('maior de idade')
```

## Composto

Formato:

```
if <condicao1>:
    <instrucao1>
else:
    <instrucao2>
```

## Aninhado ou encadeado

Formato:

```
if <condicao>:
    <instrucao>
elif <condicao>:
    <instrucao>
elif <condicao>:
    <instrucao>
else:
    <instrucao>
```

## Seletivo 

Formato:  

```
dia = 1

match dia:
    case 1:
        <instrucao>
    case 2:
        <instrucao>
    case _:
        <instrucao>
```

# Uso de operadores lógicos

Exemplos:  

```
if <condicao> and <condicao>:
    <instrucao>

if <condicao> or <condicao>:
    <instrucao>

if not <condicao>:
    <instrucao>
```
