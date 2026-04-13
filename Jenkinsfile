pipeline {
    agent any

    stages {

        stage('Setup Environment') {
            steps {
                sh '''
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                python train.py
                '''
            }
        }

        stage('Evaluate Model') {
            steps {
                sh '''
                cat outputs/metrics.json
                '''
            }
        }

        stage('Save Outputs') {
            steps {
                archiveArtifacts artifacts: 'outputs/*', fingerprint: true
            }
        }
    }
}