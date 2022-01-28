provider "aws" {
  region = "sa-east-1"
}

terraform {
  backend "s3" {
    bucket = "romaoeks-eks-eks"
    key    = "romaoeks-eks1"
    region = "us-east-1"
    encrypt = false
  }
}
