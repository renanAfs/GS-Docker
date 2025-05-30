from flask import Flask, jsonify, request, render_template_string
import psycopg2
import os
import time

app = Flask(__name__)

# Função de conexão ao banco de dados
def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'db'),
        database=os.environ.get('POSTGRES_DB'),
        user=os.environ.get('POSTGRES_USER'),
        password=os.environ.get('POSTGRES_PASSWORD')
    )
    return conn

# Função para criar a tabela (se não existir)
def init_db():
    retry_count = 5
    while retry_count:
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id SERIAL PRIMARY KEY,
                    nome VARCHAR(100),
                    email VARCHAR(100)
                );
            ''')
            conn.commit()
            cur.close()
            conn.close()
            print("Tabela 'usuarios' pronta.")
            break
        except Exception as e:
            print("Erro ao conectar ao banco. Tentando novamente...")
            print(str(e))
            retry_count -= 1
            time.sleep(2)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']

        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("INSERT INTO usuarios (nome, email) VALUES (%s, %s);", (nome, email))
            conn.commit()
            cur.close()
            conn.close()
            return jsonify({"mensagem": "Usuário cadastrado com sucesso!"}), 201
        except Exception as e:
            return jsonify({"erro": str(e)}), 500

    return render_template_string('''
        <h1>Cadastro de Usuários</h1>
        <form method="post">
            Nome: <input type="text" name="nome">
            Email: <input type="text" name="email">
            <input type="submit" value="Cadastrar">
        </form>
    ''')

@app.route('/status')
def status():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8080)
