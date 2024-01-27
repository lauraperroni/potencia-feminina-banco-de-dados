
## Comandos SQL

- **CREATE:** Utilizado para criar novas tabelas, índices, visões ou bancos de dados.

  Exemplo:
  ```sql
  CREATE TABLE usuarios (
      id INT PRIMARY KEY,
      nome VARCHAR(50),
      idade INT
  );
  ```

- **ALTER:** Permite modificar a estrutura de uma tabela existente, como adicionar, modificar ou excluir colunas.

  Exemplo:
  ```sql
  ALTER TABLE usuarios
  ADD COLUMN email VARCHAR(100);
  ```

- **DROP:** Remove objetos como tabelas, índices ou bancos de dados inteiros.

  Exemplo:
  ```sql
  DROP TABLE usuarios;
  ```

- **INSERT:** Usado para adicionar novas linhas a uma tabela existente.

  Exemplo:
  ```sql
  INSERT INTO usuarios (nome, idade)
  VALUES ('João', 30);
  ```

- **DELETE:** Remove linhas de uma tabela existente com base em uma condição especificada.

  Exemplo:
  ```sql
  DELETE FROM usuarios
  WHERE idade > 30;
  ```

- **SELECT:** Recupera dados de uma ou mais tabelas de acordo com os critérios especificados.

  Exemplo:
  ```sql
  SELECT * FROM usuarios
  WHERE idade > 25;
  ```

- **UPDATE:** Modifica os dados existentes em uma tabela.

  Exemplo:
  ```sql
  UPDATE usuarios
  SET idade = 40
  WHERE nome = 'João';
  ```

- **ORDER BY:** Ordena o resultado de uma consulta em ordem ascendente ou descendente com base em uma ou mais colunas.

  Exemplo:
  ```sql
  SELECT * FROM usuarios
  ORDER BY idade DESC;
  ```

- **LIMIT e DISTINCT:** LIMIT limita o número de linhas retornadas em uma consulta, enquanto DISTINCT remove duplicatas dos resultados.

  Exemplo:
  ```sql
  SELECT DISTINCT nome FROM usuarios;
  ```

- **GROUP BY e HAVING:** GROUP BY agrupa linhas com base em valores de coluna específicos, enquanto HAVING filtra grupos com base em uma condição especificada.

  Exemplo:
  ```sql
  SELECT idade, COUNT(*)
  FROM usuarios
  GROUP BY idade
  HAVING COUNT(*) > 1;
  ```

- **JOIN:** Combina linhas de duas ou mais tabelas com base em uma condição relacionada entre elas.

  Exemplo:
  ```sql
  SELECT *
  FROM pedidos
  INNER JOIN usuarios ON pedidos.usuario_id = usuarios.id;
  ```

- **Sub-consultas:** Consultas aninhadas dentro de uma consulta principal para realizar operações mais complexas.

  Exemplo:
  ```sql
  SELECT nome
  FROM usuarios
  WHERE idade IN (SELECT idade FROM outras_tabela);
  ```
