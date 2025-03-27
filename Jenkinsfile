# Jenkinsfile

pipeline {
    agent any
    
    stages {
        
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/ShaunCl123/WebServices.git'
            }
        }
        
        stage('Set up Python') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                sh 'source venv/bin/activate && pytest --junitxml=test_results.xml'
            }
        }
        
        stage('Package Artifacts') {
            steps {
                sh 'zip -r complete-$(date +%Y-%m-%d_%H-%M-%S).zip .'
            }
        }
    }
}
