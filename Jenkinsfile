pipeline {
    agent any

    stages {

        stage('Setup Environment') {
            steps {
                sh '''
                pip3 install -r requirements.txt
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                python3 train.py
                '''
            }
        }

        stage('Evaluate Model') {
            steps {
                sh '''
                echo "Name: Abhinav Bhagwat"
                echo "Roll No: 2022BCS0019"
                echo "----- Model Metrics -----"
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