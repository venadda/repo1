pipeline {
    agent any

    stages {
        stage('configuration') {
            steps {
                sh 'java -version'
                sh 'git --version'
                sh 'mvn -version'
            }
        }
        stage('build') {
            steps {
                build 'job11'
            }
        }
        
    }
}
