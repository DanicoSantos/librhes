## Requisitos do projeto

### Funcionalidades básicas
- [] Permitir o cadastro de livros
- [] Permitir a consulta de livros
- [] Permitir a edição de livros
- [] Permitir a remoção de livros
- [] Permitir o cadastro do mesmo livro com edições diferentes
- [] Permitir o cadastro do mesmo livro em diferentes línguas

### Funcionalidades intermediárias
- [] Permitir o cadastro, edição, listagem e remoção de usuários
- [] Permitir o empréstimo de livros com data de entrega estipulada


### Funcionalidades avançadas
- [] Notificar o atraso do livro por e-mail


### Anotações

Atributos de livro
id -> pk
title -> char
author -> char
created_at -> date
updated_at -> date
isbn -> char
genre -> fk

Atributos de genero
id -> pk
name -> char


Atributos de instância de livro
id -> pk
language -> fk
book_id -> fk
publisher -> char
publication_date -> date
created_at -> date
update_at -> date

Atributos de linguagem
id -> pk
language -> char







