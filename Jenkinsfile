pipeline {
    agent {
        label 'master'

    }
    tools {
           dockerTool 'myDocker'
    }
    stages {
    stage ('Check out the code') {

        steps{
            git branch: 'master', url: 'https://github.com/mathewg1983/dockerProject.git'
        }

    }
    stage ('Compile the code') {

        steps {
	    
            
	    sh """
            sudo docker-compose up -d
	    sed "build_container_version=${env.BUILD_NUMBER}" .env
            cat .env 	
            """
        }

    }
 }
}
