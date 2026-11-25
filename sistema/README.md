# Agenda de Consultas

Versão em construção. Etapa atual: banco de dados (`banco.py`).

## Etapas

- [x] Etapa 1 — banco de dados (parcial: conexão, listagem e cadastro)
- [ ] Etapa 2 — backend (validações)
- [ ] Etapa 3 — frontend (tela Tkinter)

## Funções do banco

| Função | Operação | Status |
|---|---|---|
| `conectar()` | abre o banco e cria a tabela | pronto |
| `listar()` | lista as consultas | pronto |
| `inserir()` | cadastra uma consulta | pronto |

Edição (`UPDATE`) e exclusão (`DELETE`) ficam para depois.

## Teste rápido

```bash
python -c "import banco; c = banco.conectar(); banco.inserir(c, ['123456789012345','Ana Silva','Dra. Lima','25/12/2026','14:30','Retorno']); print(banco.listar(c))"
```
