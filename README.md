# Analisador Léxico
 ## 1. Crie Tokens apropriados e para cada Token faça uma Expressão Regular para a
  Linguagem **A**. A Linguagem **A** é definida a partir da Linguagem C, as características da **A** são: 
- Possui apenas os tipos de dados int e string;
- Não possui laços de repetição;
- Possui a instrução if-else, tal qual a Linguagem C;
- Cada função da A tem no máximo dois parâmetros;
- As demais características são idênticas ao C, inclusive a sintaxe;

Analisador Léxico  crislanio.wordpress.com
Scripts feito com Python

## Dependências
- Python2 +

# Alguns objetivos

- Implementação de um algoritmo que recebe como entrada um NFA e retorna um Autômato Finito Determinístico (DFA). A forma de representação dos Autômatos é livre, ou seja, você pode representá-los como matriz, lista, dicionário etc.

- Utilizando o DFA da acima, é implementado um analisador léxico para a Linguagem **A**. É feito um arquivo .txt contendo a lista de tokens utilizados e o que eles representam. O arquivo tem o seguinte formato: cada linha contém duas informações separadas por espaço, sendo a primeira posição o token e a segunda o que ele representa. Se o token representa mais de uma entidade, separe-os por vírgula. 


## Entrada
- A entrada é composta por um código fonte de um programa qualquer escrito em A.
## Saída
- Para cada entrada, seu programa deve produzir uma sequência de Tokens ou a palavra **ERRO**, casa a entrada tenha erro léxico.

## Exemplo
## Entrada
- int a = 0 ;
- in b = 5 + a ;
- string c = “teSte” ;
## Saída
- INT VAR EQ NUM SEMICOLON
- INT VAR EQ NUM ADD VAR SEMICOLON
- STRING VAR EQ CONST SEMICOLON
### Screenshots
![alt tag](https://raw.githubusercontent.com/crislanio/Analisador-L-xico/master/Screenshot%20at%202017-05-18%2023:12:38.png)

