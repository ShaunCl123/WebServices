pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/ShaunCl123/WebServices.git'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                bat 'C:\\Users\\yuiku\\AppData\\Local\\Programs\\Python\\Python310\\python.exe -m venv venv'
                bat 'venv\\Scripts\\activate'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\pytest'
            }
        }
    }
}
