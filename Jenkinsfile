pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = "localhost:5000"
        IMAGE_NAME = "guestbook"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/geo-petrini/guestbook'
            }
        }

        // stage('Install Dependencies') {
        //     steps {
        //         pip install -r requirements.txt
        //     }
        // }

        // stage('Run Tests') {
        //     steps {
        //         sh 'make test'
        //         // se il comando dei test esce con errore, Jenkins blocca la pipeline
        //     }
        // }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_REGISTRY}/${IMAGE_NAME}:latest")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry("http://${DOCKER_REGISTRY}", '') {
                        docker.image("${DOCKER_REGISTRY}/${IMAGE_NAME}:latest").push()
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline eseguita correttamente'
        }
        failure {
            echo 'Pipeline fallita'
        }
    }
}
