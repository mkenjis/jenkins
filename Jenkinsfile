pipeline {
    agent { 
        dockerfile {
            label 'flask_python_img'
	}
    }
    stages {
        stage('Test') {
            steps {
                sh 'python -version'
            }
        }
    }
}
