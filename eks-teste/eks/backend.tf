provider "aws" {
  
}

terraform {
  backend = "s3"
  config = {
    bucket = "romaoeks-eks-eks"
    key = "romaoeks-eks1"
    region = "sa-east-1"
    encrypt = false
    #dynamodb_table = "testando"
  }
}
