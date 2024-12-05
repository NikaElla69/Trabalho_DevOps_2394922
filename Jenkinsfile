pipeline {
    agent any
    stages {
        stage('Clonar Repositório') {
            steps {
                git 'https://github.com/NikaElla69/Trabalho_DevOps_2394922.git'
            }
        }
        stage('Rodar Testes') {
            steps {
                sh 'python3 -m unittest discover -s app -p "test_app.py"'
            }
        }
        stage('Build e Deploy') {
            steps {
                sh 'docker-compose up --build -d'
            }
        }
    }
}
