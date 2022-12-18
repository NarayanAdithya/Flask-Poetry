@Library('poetry-jenkins-library')
@Library('python-app-library')

def version
pipeline {
    agent any
    stages{
        stage("Install"){
            steps{
                script{
                    poetryInstall()
                }
            }
        }
        stage("Lint"){
            steps{
                script{
                    poetryLint()
                }
            }
        }
        stage("Bandit"){
            steps{
                script{
                    poetryBandit()
                }
            }
        }
        stage("Test"){
            steps{
                script{
                    poetryTest()
                }
            }
        }
        stage("IncVersion"){
            steps{
                script{
                    poetryBump()
                }
            }
        }
        stage("MakeVersionCommit"){
            steps{
                script{
                    version=getVersion("pyproject.toml")
                    makeupdatecommit("Flask-Poetry")
                }
            }
        }
        tage("Build Image"){
            steps{
                script{
                    buildDockerImage(version,"flaskpoetry")
                }
            }
        }
        stage("Login"){
            steps{
                script{
                    dockerLogin()
                }
            }
        }
        stage("Push Artifact"){
            steps{
                script{
                    dockerPush(version,"flaskpoetry")
                }
            }
        }

    }
}