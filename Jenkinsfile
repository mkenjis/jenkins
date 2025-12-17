pipeline {
    agent none
    stages {
        stage('Build') {
            agent any 
            steps {
	        sh 'docker image build -t python_flask_img .'
                sh 'docker image ls'
		sh 'echo "DOCKER_USER is $DOCKER_USER"'
		sh 'echo "Trustn0" | docker login --username mkenjis --password-stdin'
		sh 'docker image push python_flask_img'
            }
        }
    }
}
