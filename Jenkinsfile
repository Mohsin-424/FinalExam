pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "finalexam-ml-model" // Docker image name
        CONTAINER_NAME = "finalexam-ml-model-container" // Docker container name
        GITHUB_REPO = "https://github.com/Mohsin-424/FinalExam.git" // Repository URL
    }
    stages {
        // Clone the Git Repository
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: "${GITHUB_REPO}" // Pull code from the main branch
            }
        }

        // Build the Docker Image
        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker Image: ${DOCKER_IMAGE}"
                    // Ensure the Dockerfile and app.py are in the root directory
                    sh 'docker build -t $DOCKER_IMAGE .' // Adjust the context path if needed
                }
            }
        }

        // Deploy using Terraform
        stage('Deploy with Terraform') {
            steps {
                script {
                    echo "Deploying infrastructure using Terraform..."
                    sh '''
                    cd terraform
                    terraform init
                    terraform apply -auto-approve
                    '''
                }
            }
        }

        // Test the Deployment
        stage('Test Deployment') {
            steps {
                script {
                    echo "Testing the deployment..."
                    // Adding a delay to ensure container starts properly
                    sh '''
                    sleep 10 # Wait for the container to start
                    curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"features": [2]}'
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Pipeline failed. Check the logs for errors.'
        }
    }
}
