pipeline {
	agent any 
		stages{
			stage('One'){
				steps{
					echo "Hi from Javad"
				     }
			}
			stage('Two'){
				steps{
					input('Do you want to proceed?')
				}
			}
			stage('Three'){
				when{
				    not {
					    branch "master"
					}
                                    }				    
                                steps{
				     echo('Stage Three')
				     }
			}
			stage('Four'){
				parallel{
					stage('Unit test'){
						steps{
						     echo 'Running the Unit test'
						}
                                             }
					stage('Integration test'){
						steps {
							echo 'Running Integration test'
						      }
                                                    }
				     } 
			       	}
    		}
}

