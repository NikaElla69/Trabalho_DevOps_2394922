from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configuração do Banco de Dados
db_config = {
    'host': 'mariadb',
    'user': 'root',
    'password': 'root',
    'database': 'alunos_db'
}

# Rota para cadastrar aluno
@app.route('/cadastrar', methods=['POST'])
def cadastrar_aluno():
    data = request.json
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = "INSERT INTO alunos (nome, ra) VALUES (%s, %s)"
        cursor.execute(query, (data['nome'], data['ra']))
        conn.commit()
        return jsonify({'message': 'Aluno cadastrado com sucesso!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
