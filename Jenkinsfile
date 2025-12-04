pipeline {
    agent none
    stages {
        stage('Build') {
            agent any
            steps {
	        sh 'docker image build -t python_flask_img .'
                sh 'docker image ls'
            }
        }
    }
}
