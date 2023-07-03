pipeline {
    agent { dockerfile true}
    stages {
        stage('Test'){
            steps {
                sh 'pytest /app/test_app.py'
                sh 'ls -al'
            }
        }
    }

}