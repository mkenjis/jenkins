pipeline {
    agent none
    stages {
        stage('Build') {
	    steps {
	        sh 'docker image build -t python_img .'
	    }
	}
        stage('Test') {
            steps {
                sh 'python -version'
            }
        }
    }
}
