from conexao import Conexao

conexaoBD = Conexao("localhost", "root", "mysql", "")

conexaoBD.manipular("CREATE DATABASE biblioteca")

conexaoBD.manipular("CREATE TABLE")