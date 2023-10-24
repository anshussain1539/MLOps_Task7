def customFunctions

pipeline {
    agent any

    stages {
        stage('Load Functions') {
            steps {
                script {
                    customFunctions = load 'jenkinsFunctions.groovy'
                }
            }
        }

        stage('checkout') {
            steps {
                script {
                    def repoUrl = 'https://github.com/anshussain1539/MLOps_Task7.git'
                    def branch = 'main'
                    customFunctions.checkoutCode(repoUrl, branch)
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    customFunctions.buildProject()
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    customFunctions.runTests()
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    customFunctions.deployApplication()
                }
            }
        }
    }
}
