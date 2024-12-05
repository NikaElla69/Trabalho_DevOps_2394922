# Trabalho_DevOps_2394922
Trabalho de DevOps - Camilla Gomes e Pedro Vieira
Camilla: 23.9492-2
Pedro: 21.5985-3


## Visão Geral
Este projeto implementa uma aplicação Flask integrada com MariaDB, monitorada por Prometheus e Grafana, utilizando um pipeline CI/CD no Jenkins.

---

## Estrutura do Repositório
├── app/ 
│ ├── main.py # Código principal da aplicação Flask 
│ ├── db_config.py # Configuração do banco de dados 
│ └── test_app.py # Teste unitário 
├── db/ 
│ └── init.sql # Script de inicialização do banco 
├── grafana/ 
│ └── dashboard.json # Configuração da dashboard do Grafana 
├── prometheus/ 
│ └── prometheus.yml # Configuração do Prometheus 
├── Dockerfile # Dockerfile para a aplicação Flask 
├── docker-compose.yml # Arquivo de configuração Docker Compose 
├── Jenkinsfile # Pipeline do Jenkins 
└── README.md # Instruções do projeto


---

## Pré-requisitos
1. **Docker** e **Docker Compose** instalados.
2. **Jenkins** configurado para pipelines baseados em `Jenkinsfile`.
3. **Git** configurado e repositório clonado.

---

## Passos para Executar

### 1. Configurar o Banco de Dados
Certifique-se de que o arquivo `db/init.sql` contém o script de criação do banco.
O MariaDB será inicializado automaticamente pelo `docker-compose`.

### 2. Rodar o Ambiente com Docker Compose
Suba os serviços:
	```bash```
	docker-compose up --build

Verifique se os seguintes serviços estão funcionando:
	Aplicação Flask: http://localhost:5000
	Prometheus: http://localhost:9090
	Grafana: http://localhost:3000

### 3. Configurar o Grafana
Faça login no Grafana:
	Usuário: admin
	Senha: admin
Importe a dashboard de grafana/dashboard.json.


### 4. Configurar o Jenkins
No Jenkins, configure um novo pipeline apontando para este repositório.
A pipeline seguirá as etapas do arquivo Jenkinsfile:
	Clonar o código do Git.
	Rodar os testes unitários.
	Build e Deploy da aplicação.


### 5. Testes Unitários
Para rodar os testes unitários:
	**python -m unittest discover -s app -p "test_*.py"**

*Problemas Conhecidos*
	Certifique-se de que as portas 5000, 9090 e 3000 estão livres.
	Erros de conexão com o banco podem ser causados por variáveis de ambiente mal configuradas no docker-compose.yml.

