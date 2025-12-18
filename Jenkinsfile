pipeline {
    agent none
    stages {
        stage('Build') {
            agent any 
            steps {
	        sh 'docker image build -t mkenjis/python_flask_img .'
                sh 'docker image ls'
		sh 'echo "DOCKER_USER is $DOCKER_USER"'
		sh 'echo $DOCKER_PWD | docker login --username $DOCKER_USER --password-stdin'
		sh 'docker image push --quiet mkenjis/python_flask_img'
            }
        }
    }
}
