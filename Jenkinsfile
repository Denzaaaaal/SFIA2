pipeline {
    agent any

    stages{
        stage('Development Environment') {
            steps{
                sh 'chmod +x ./scripts/*'
                sh './scripts/dependencies.sh'
                sh './scripts/run.sh'
            }
        }
        // stage('Testing'){
        //     steps{
        //         sh 'pytest ./test/testing.py'
        //     }
        // }
    }
}