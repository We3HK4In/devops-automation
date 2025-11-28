pipeline {
    agent any
    tools{
        maven 'maven_3_5_0'
    }
    stages{
        stage('Build Maven'){
            steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/We3HK4In/devops-automation/']]])
                sh 'mvn clean install'
            }
        }
    

        stage('tochange - Build docker image'){
            steps{
                script{
                    sh 'docker build -t d0ckbl0cker/python-simple-app:latest .'
                }
            }
        }
        stage('tochange - Login to Dockerhub & Push image to Hub'){
            steps{
                script{
                   withCredentials([string(credentialsId: 'dockerhub-pwd', variable: 'dockerhubpwd')]) {
                   sh 'docker login -u d0ckbl0cker -p ${dockerhubpwd}'

}
                   sh 'docker push d0ckbl0cker/wtv-repo'
                }
            }
        }
        /*stage('Deploy to k8s'){
            steps{
                script{
                    kubernetesDeploy (configs: 'deploymentservice.yaml',kubeconfigId: 'k8sconfigpwd')
                }
            }
        }*/
    }
}
