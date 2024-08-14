#Importar a classe Conexão
from Conexao import Conexao

#Instanciar um objeto de Conexão
conexaoBD = Conexao("localhost", "root", "mysql", "")

versao = conexaoBD.consultar("SELECT VERSION()")
print(versao[0][0])
#Criar banco
conexaoBD.manipular("CREATE DATABASE bancoteste")

#Criar tabela
conexaoBD.manipular("CREATE TABLE bancoteste.livro")

#Preencher tabela