pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Cloning the Git repository containing Jenkinsfile and index.html
                git branch: 'main', url: 'https://github.com/saadbhatti763/jenkins_demo.git'
            }
        }

        stage('Copy Files to /var/www/html') {
            steps {
                // Copy Jenkinsfile and index.html to /var/www/html using sudo without password prompt
                sh '''
                sudo cp -r Jenkinsfile index.html /var/www/html/
                '''
            }
        }
    }

    post {
        success {
            echo 'Deployment Successful!'
        }
        failure {
            echo 'Deployment Failed.'
        }
    }
}
