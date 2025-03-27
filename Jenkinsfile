pipeline {
    agent any

    environment {
        PATH = "C:\\Users\\yuiku\\AppData\\Local\\Programs\\Python\\Python310;${PATH}"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/ShaunCl123/WebServices.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'C:\\Users\\yuiku\\AppData\\Local\\Programs\\Python\\Python310\\python.exe -m pip install --upgrade pip'
                bat 'C:\\Users\\yuiku\\AppData\\Local\\Programs\\Python\\Python310\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'C:\\Users\\yuiku\\AppData\\Local\\Programs\\Python\\Python310\\python.exe -m pytest'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the application...'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
