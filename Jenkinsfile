pipeline {
    agent any

    stages{
        stage('Development Environment') {
            steps{
                sh 'chmod +x ./scripts/*'
                sh './scripts/before_installation.sh'
                sh './scripts/installation.sh'

            }
        }
        stage('Testing'){
            steps{
                sh 'pytest ./test/testing.py'
            }
        }
    }
}