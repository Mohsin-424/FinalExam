pipeline {
    agent any

    environment {
        APP_PATH = '/path/to/your/app'
        REMOTE_SERVER = 'your-server-ip'
        REMOTE_USER = 'your-username'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Mohsin-424/FinalExam.git'  // Replace with your GitHub repository URL
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo 'No tests added yet'
                }
            }
        }

        stage('Deploy to Server') {
            steps {
                script {
                    // Transfer the app to the server using SCP
                    sh "scp -r ./ user@${REMOTE_SERVER}:${APP_PATH}"

                    // SSH into the server to deploy
                    sh "ssh ${REMOTE_USER}@${REMOTE_SERVER} 'cd ${APP_PATH} && pip install -r requirements.txt && gunicorn -w 4 app:app --bind 0.0.0.0:5000 &'"
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment completed successfully!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
