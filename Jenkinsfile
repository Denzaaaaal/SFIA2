pipeline {
    agent any

    stages{
        stage('Development Environment') {
            steps{
                sh 'chmod +x ./scripts/*/*'
                sh './scripts/deployment/dependencies.sh'
                sh './scripts/deployment/run.sh'
            }
        }
        stage('Testing') {
            steps{
                sh 'sleep 15'
                sh 'pytest ./scripts/testing/url_testing.py'
            }
        }
    }
}