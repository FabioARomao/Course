terraform {
    backend "s3" {
    bucket = "romaoeks-eks-eks"
    encrypt = false
    key = "idiota"
    region = "sa-east-1"
    #profile = "terraeks" # you have to give the profile name here. not the variable("${var.AWS_PROFILE}")
  }
}