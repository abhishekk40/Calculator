pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                dockerfile {
      filename 'Dockerfile'
    }
            }
            steps {
                sh 'python -m py_compile calculator.py'
                stash(name: 'compiled-results', includes: '*.py*')
            }
        
        
            
        }
    }
}
