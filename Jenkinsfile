pipeline {
    agent any
    stages{
        stage('Anis - Build docker image'){
            steps{
                script{
                    sh 'docker build -t d0ckbl0cker/python-simple-app:Recording .'
                }
            }
        }
        stage('Anis - Login to Dockerhub & Push image to Hub'){
            steps{
                script{
                   withCredentials([string(credentialsId: 'dockerhub-pwd', variable: 'dockerhubpwd')]) {
                       sh 'docker login -u d0ckbl0cker -p ${dockerhubpwd}'
                    }
                   sh 'docker push d0ckbl0cker/wtv-repo'
                }
            }
        }
    }
}
