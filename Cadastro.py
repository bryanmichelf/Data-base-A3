import sqlite3

def tabela_jornada_academica():
    conn = sqlite3.connect('jornada_academica.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expositor (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            uc TEXT NOT NULL,
            periodo TEXT,
            curso TEXT,
            titulo TEXT NOT NULL,
            tipo_trabalho TEXT CHECK (tipo_trabalho IN ('extensão', 'pesquisa')),
            localizacao TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos_envolvidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ra TEXT UNIQUE NOT NULL,
            nome TEXT NOT NULL,
            expositor_id INTEGER,
            FOREIGN KEY (expositor_id) REFERENCES expositor(id) ON DELETE CASCADE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS visitantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT
        )
    ''')

    conn.commit()
    conn.close()

def inserir_expositor(uc, periodo, curso, titulo, tipo_trabalho, localizacao): 
    conn = sqlite3.connect('jornada_academica.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO expositor 
        (uc, periodo, curso, titulo, tipo_trabalho, localizacao) 
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (uc, periodo, curso, titulo, tipo_trabalho, localizacao))

    conn.commit()
    conn.close()

def inserir_alunos_envolvidos(ra, nome, expositor_id):
    conn = sqlite3.connect('jornada_academica.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO alunos_envolvidos
        (ra, nome, expositor_id) 
        VALUES (?, ?, ?)
    ''', (ra, nome, expositor_id))

    conn.commit()
    conn.close()

def inserir_visitantes(nome, email):
    conn = sqlite3.connect('jornada_academica.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO visitantes
        (nome, email)
        VALUES (?, ?)
    ''', (nome, email))

    conn.commit()
    conn.close()  

def atualizar_expositor(id, uc, periodo, curso, titulo, tipo_trabalho, localizacao):
    conn = sqlite3.connect('jornada_academica.db')
    cursor = conn.cursor()

    cursor.execute('''  
        UPDATE expositor 
        SET uc = ?, periodo = ?, curso = ?, titulo = ?, tipo_trabalho = ?, localizacao = ?
        WHERE id = ?
    ''', (uc, periodo, curso, titulo, tipo_trabalho, localizacao, id))

    conn.commit()
    conn.close()

def atualizar_alunos_envolvidos(id, ra, nome, expositor_id):
    conn = sqlite3.connect('jornada_academica.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE alunos_envolvidos 
        SET ra = ?, nome = ?, expositor_id = ?
        WHERE id = ?
    ''', (ra, nome, expositor_id, id))

    conn.commit()
    conn.close()

def atualizar_visitantes(id, nome, email):
    conn = sqlite3.connect('jornada_academica.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE visitantes           
        SET nome = ?, email = ?
        WHERE id = ?
    ''', (nome, email, id))

    conn.commit()
    conn.close()

def consultar_expositores():
    conn = sqlite3.connect('jornada_academica.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM expositor (?)
                   ''')
    expositores = cursor.fetchall()

    conn.close()
    return expositores

def consultar_alunos_envolvidos():
    conn = sqlite3.connect('jornada_academica.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM alunos_envolvidos (?)
                    ''')
    alunos = cursor.fetchall()

    conn.close()
    return alunos

def consultar_visitantes():
    conn = sqlite3.connect('jornada_academica.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM visitantes (?)
                   ''')
    visitantes = cursor.fetchall()

    conn.close()
    return visitantes

def deletar_expositor(id):
    conn = sqlite3.connect('jornada_academica.db')
    cursor = conn.cursor()

    cursor.execute('''
        DELETE FROM expositor 
        
        WHERE id = ?', (id,)
                   
        ''')
    
    conn.commit()
    conn.close()

def deletar_alunos_envolvidos(id):
    conn = sqlite3.connect('jornada_academica.db')
    cursor = conn.cursor()

    cursor.execute('''
        DELETE FROM alunos_envolvidos 
    
        WHERE id = ?', (id,)
                   
        ''')
    
    conn.commit()
    conn.close()

def deletar_visitante(id):
    conn = sqlite3.connect('jornada_academica.db')
    cursor = conn.cursor()

    cursor.execute('''
        DELETE FROM visitantes 
                   
        WHERE id = ?', (id,)
                   
     ''')
    
    conn.commit()
    conn.close()

    

        