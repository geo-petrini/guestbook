pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = "localhost"
        IMAGE_NAME = "guestbook"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url:'https://github.com/geo-petrini/guestbook'
            }
        }

        // stage('Install Dependencies') {
        //     steps {
        //         pip install -r requirements.txt
        //     }
        // }

        // stage('Test code') {
        //     steps {
        //         sh 'make test'
        //         // se il comando dei test esce con errore, Jenkins blocca la pipeline
        //     }
        // }

        stage('Build Docker Image') {
            steps {
                script {
                     // oppure usare ${env.BUILD_NUMBER} invece di latest
                     //docker.build("${DOCKER_REGISTRY}/${IMAGE_NAME}:${env.BUILD_NUMBER}")
                    docker.build("${DOCKER_REGISTRY}/${IMAGE_NAME}:latest")
                }
            }
        }
    //    stage('Test application') {
    //         steps {
    //             sh 'docker run --rm ${IMAGE_NAME}:latest ./run-tests.sh'
    //         }
    //     }
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
