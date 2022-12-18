@Library('poetry-jenkins-library')_

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

    }
}