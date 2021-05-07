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
            echo
            echo "${DOCPASS}" | sudo docker login --username ${DOCUSERN} --password-stdin
            sudo docker-compose push docpush 	
            """
        }

    }
 }
}
