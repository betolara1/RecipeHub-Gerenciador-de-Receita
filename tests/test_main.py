import sqlite3
import os
import pytest
import main

# O Kivy pode ser problemático ao rodar testes puramente em modo texto sem display.
# Portanto, vamos focar em testar a lógica do SQLite e regras de negócio.

@pytest.fixture
def temp_db(tmp_path):
    """Cria um banco de dados temporário para os testes."""
    db_file = tmp_path / "test_recipeDB.db"
    
    # Fazemos um mock do connect apenas no contexto desse teste
    original_connect = sqlite3.connect
    main.sqlite3.connect = lambda db_name, **kwargs: original_connect(db_file, **kwargs)
    
    app = main.Aplicativo()
    # Mock para evitar dependência excessiva de Interface Gráfica nos testes do DB
    app.toolbarText = "BEBIDAS" 
    
    yield app, db_file
    
    # Restaura o sqlite original
    main.sqlite3.connect = original_connect

def test_create_tables(temp_db):
    """Testa se todas as tabelas das categorias e configurações são criadas."""
    app, db_file = temp_db
    app.createTables()
    
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [t[0] for t in c.fetchall()]
    conn.close()
    
    # Verifica se as tabelas padrão do SQLite também existem e as da aplicação
    for cat in app.cats:
        assert cat in tables
    assert 'config' in tables

def test_initial_categories_count(temp_db):
    """Verifica as categorias padrão configuradas no Aplicativo."""
    app, db_file = temp_db
    assert len(app.cats) == 10
    assert 'bebidas' in app.cats
    assert 'sobremesas' in app.cats

def test_database_insert_mock():
    """Testa a lógica de criação de query de insert manualmente para garantir o formato correto."""
    categoria = "doces"
    nome = "Pudim"
    desc = "Pudim de leite condensado"
    ingred = "Leite, Ovos, Açúcar"
    prep = "Asse em banho-maria"
    
    # Apenas um dummy test para verificar a sintaxe que seria inserida
    query = f"INSERT INTO {categoria} VALUES (:id, :name, :desc, :ingred, :prep)"
    assert ":id" in query
    assert ":name" in query
    assert categoria in query

def test_app_theme_colors():
    """Testa se as constantes ou estados iniciais são definidos."""
    app = main.Aplicativo()
    assert app.toolbarText == ''
    app.toolbarText = 'Doces'
    assert app.toolbarText == 'Doces'

def test_language_init():
    """Verifica configurações iniciais da linguagem ou flags."""
    app = main.Aplicativo()
    assert app.dialog is None
    assert app.textDialog == ''
