pipeline {
    agent {
        label 'master'

    }
    tools {
            maven 'myMaven'
            jdk 'myJDK'
	    dockerTool 'myDocker'
    }
    stages {
    stage ('Check out the code') {

        steps{
            git branch: 'master', url: 'https://github.com/gladiotuetur/dockerProject.git'
        }

    }
    stage ('Compile the code') {

        steps {
            sh """
            sudo docker-compose up -d
            """
        }

    }
 }
}
