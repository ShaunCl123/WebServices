pipeline {
    agent any

    environment {
        APP_NAME = 'Inventory'
    }

    stages {
        stage('Checkout') {
            steps {
                bat 'git clone https://github.com/your-repo/Inventory.git'
            }
        }

        stage('Build') {
            steps {
                bat 'echo Building the project...'
                bat 'gradlew.bat build' // Use the Windows version of Gradle if applicable
            }
        }

        stage('Test') {
            steps {
                bat 'echo Running tests...'
                bat 'python -m unittest discover' // Ensure Python is installed and in PATH
            }
        }

        stage('Package') {
            steps {
                bat 'echo Packaging application...'
                bat 'jar -cvf %APP_NAME%.jar -C build/libs .' // Adjust if packaging differently
            }
        }

        stage('Deploy') {
            steps {
                bat 'echo Deploying application...'
                bat 'copy %APP_NAME%.jar C:\\deploy\\' // Adjust path for deployment location
            }
        }
    }

    post {
        success {
            bat 'echo Build and deployment successful!'
        }
        failure {
            bat 'echo Build failed. Check logs for details.'
        }
    }
}
