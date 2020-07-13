pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                dockerfile {
      filename 'Dockerfile'
    }
            }
            
        
            stage('Test'){
                echo " Testing"
            }
            
        }
    }
}
