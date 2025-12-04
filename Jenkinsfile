pipeline {
    agent none
    stages {
        stage('Build') {
            agent { label 'agent1' }
            steps {
	        sh 'docker image build -t python_flask_img .'
                sh 'docker image ls'
            }
        }
    }
}
