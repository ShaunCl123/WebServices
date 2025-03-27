pipeline {
    agent any

    environment {
        PYTHON_HOME = "C:\\Users\\yuiku\\AppData\\Local\\Programs\\Python\\Python310"  // Update this with your Python path
        PATH = "${PYTHON_HOME};${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Assuming you may need some dependencies, like requests or any other libraries
                    sh 'pip install -r requirements.txt'  // If you don't need this step, you can comment it out
                }
            }
        }

        stage('Test Methods') {
            steps {
                script {
                    // Now we will test the methods directly in the pipeline
                    def code = """
                    import your_module  # Replace with actual module name

                    def test_getSingleProduct():
                        try:
                            result = your_module.getSingleProduct(1)
                            assert result is not None, "Test Failed: getSingleProduct returned None"
                            assert 'name' in result, "Test Failed: 'name' key not found in getSingleProduct result"
                            print("test_getSingleProduct passed")
                        except Exception as e:
                            print(f"test_getSingleProduct failed: {str(e)}")

                    def test_getAll():
                        try:
                            result = your_module.getAll()
                            assert isinstance(result, list), "Test Failed: getAll did not return a list"
                            assert len(result) > 0, "Test Failed: getAll returned an empty list"
                            print("test_getAll passed")
                        except Exception as e:
                            print(f"test_getAll failed: {str(e)}")

                    # Run tests
                    test_getSingleProduct()
                    test_getAll()
                    """
                    writeFile file: 'test_methods.py', text: code
                    sh 'python test_methods.py'  // Running the test script directly
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up after pipeline'
            // Clean up code here if necessary
        }

        success {
            echo 'Pipeline finished successfully!'
        }

        failure {
            echo 'Pipeline failed.'
        }
    }
}
