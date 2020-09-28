pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:3.8-alpine' alwaysPull true
                }
            }
            steps {
                sh 'python -m py_compile test_calculator.py' 
                stash(name: 'compiled-results', includes: '*.py*') 
            }
        }
    }
}
        
        
