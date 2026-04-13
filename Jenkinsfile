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
                echo "Model evaluation completed. Check metrics.json"
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