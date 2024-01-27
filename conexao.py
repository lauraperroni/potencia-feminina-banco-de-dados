import sqlite3                      # importando a biblioteca

conexao = sqlite3.connect('bancoLaura')  # conexão do arquivo python com o banco de dados
cursor = conexao.cursor()                # passando a conexão para uma outra variável

 # executa os comandos
cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')                 
cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));') 
cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')
cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')
cursor.execute('DROP TABLE produtos')
cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(1,"Laura","Brasil","Laura@gmail.com",123456789);')
cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(2,"Julia","Brasil","julia@gmail.com",123456789);')
cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(3,"Marcia","Brasil","marcia@gmail.com",123456789);')
cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(4,"Thais","Brasil","thais@gmail.com",123456789);')
cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(6,"Thais","Brasil","thais@gmail.com",123456789);')
cursor.execute('DELETE FROM usuario WHERE id = 5;')
dados = cursor.execute('SELECT * FROM usuario ORDER BY nome DESC;')
for usuario in dados:
    print(usuario)
cursor.execute('UPDATE usuario SET email="laura@gmail.com" WHERE nome="Laura";')
dados = cursor.execute('SELECT * FROM usuario GROUP BY name HAVING id>3')
dados = cursor.execute('SELECT * FROM usuario GROUP BY name HAVING id>3')

cursor.execute('CREATE TABLE gerentes(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')                 
cursor.execute('INSERT INTO gerentes(id,nome,endereco,email) VALUES(2,"Cacau","Brasil","cacau@gmail.com");')
dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerentes ON usuario.id = gerentes.id;')

dados = cursor.execute('SELECT * FROM usuario WHERE nome IN (SELECT nome FROM gerentes);')



conexao.commit()                    # envia a conexão
conexao.close                       # fecha a conexão
