pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t myapp .'
            }
        }

        stage('Run') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Test') {
            steps {
                script {
                    def containerId = sh(
                        script: 'docker ps -q --filter "ancestor=myapp"',
                        returnStdout: true
                    ).trim()

                    def exitCode = sh(
                        script: "docker inspect --format='{{.State.ExitCode}}' ${containerId}",
                        returnStatus: true
                    )

                    if (exitCode != 0) {
                        error "Tests failed! Exit code: ${exitCode}"
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                sh 'docker-compose down'
                sh 'docker-compose push'
            }
        }
    }
}