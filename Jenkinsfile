pipeline {
    agent any

    environment {
        VENV_PATH = 'venv'                         // Virtual environment folder
        REQUIREMENTS_FILE = 'requirements.txt'      // Path to requirements file
        SERVER_PATH = 'C:\\FastAPI-Project'         // Change to your project folder (if necessary)
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Clones the GitHub repository to the workspace
                git branch: 'main', url: 'https://github.com/ShaunCl123/WebServices.git'
            }
        }

        stage('Set Up Python Virtual Environment') {
            steps {
                bat '''
                python -m venv %VENV_PATH%
                call %VENV_PATH%\\Scripts\\activate
                pip install --upgrade pip
                pip install -r %REQUIREMENTS_FILE%
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call %VENV_PATH%\\Scripts\\activate
                pytest > test_results.txt
                '''
            }
        }

        stage('Start FastAPI Server') {
            steps {
                bat '''
                call %VENV_PATH%\\Scripts\\activate
                uvicorn main:app --host 0.0.0.0 --port 8000 --reload
                '''
            }
        }
    }

    post {
        success {
            echo "🚀 Build successful!"
        }
        failure {
            echo "❌ Build failed. Check the logs."
        }
    }
}
