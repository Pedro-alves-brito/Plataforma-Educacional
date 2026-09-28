# Estrutura de ramificação do template

O `index.html` funciona como modelo estrutural de todas as páginas: cabeçalho, navegação, conteúdo modular e rodapé.

## Páginas sugeridas

```text
/
├── index.html
├── professores.html
├── disciplinas.html
├── solicitar-reforco.html
├── ser-voluntario.html
├── blog.html
├── faq.html
├── paginas.html
├── portfolios.html
├── style.css
└── assets/
    ├── logo.png
    ├── banner-principal.png
    ├── banner-secundario.png
    └── banner-terciario.png
```

## Como ramificar cada página

- `professores.html`: reutilizar Header/Footer e trocar o conteúdo central por filtros + grid de cards + modelo de perfil detalhado.
- `disciplinas.html`: reutilizar Header/Footer e trocar o conteúdo central por categorias, tabela/cards de disciplinas e bloco de detalhes por disciplina.
- `solicitar-reforco.html`: reutilizar Header/Footer e adicionar formulário visual com campos do pedido de reforço.
- `ser-voluntario.html`: reutilizar Header/Footer e adicionar formulário de cadastro + seção visual “Como Funciona” com 5 passos.
- `blog.html`: reutilizar Header/Footer e transformar a prévia do blog em grid completo de artigos.
- `faq.html`: reutilizar Header/Footer e utilizar o componente Accordion do Bootstrap 5.
- `paginas.html`: concentrar conteúdos institucionais e a página prática do 1º bimestre (tabelas, listas, âncoras, mapeamento de imagens, links etc.).
- `portfolios.html`: manter a mesma identidade e listar os portfólios individuais dos integrantes.

## Regra visual

Todas as páginas devem manter as mesmas variáveis de cor e os mesmos padrões de `.site-header`, `.site-navbar`, `.section-space` e `.site-footer` definidos no `style.css`.
