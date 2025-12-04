pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
	        sh 'docker image build -t python_flask_img .'
                sh 'docker image ls'
            }
        }
    }
}
