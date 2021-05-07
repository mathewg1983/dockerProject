pipeline {
    agent {
        label 'master'

    }
    environment {
        DOCUSERN = credentials('jenkins-docker-secret-key-id')
        DOCPASS = credentials('jenkins-docker-secret-access-key')
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
	    rm -f .env
            echo "build_container_version=${env.BUILD_NUMBER}" >> .env
            sudo docker-compose up -d app
            docker login --username ${env.DOCUSERN} --password ${env.DOCPASS}
            sudo docker-compose push docpush 	
            """
        }

    }
 }
}
