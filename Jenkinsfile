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
        stage(" Print version"){
            steps{
                script{
                    getVersion("pyproject.toml")
                }
            }
        }

    }
}