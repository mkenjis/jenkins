pipeline {
    agent none
    stages {
        stage('Test') {
	    agent {
	        docker { image 'python:3.8-alpine' }
	    }
            steps {
                sh 'python -version'
            }
        }
    }
}
