pipeline {
  agent { label 'master'}
  stages {
    stage('test') {
      git ([url: "git@github.com:hari09kg1a0403/stupid_code_python.git", branch: "master", changelog:true])
      sh "pwd"
    }
  } 
}
