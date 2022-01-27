terraform {
  backend "s3" {
    bucket = "romaoeks-eks-eks"
    key    = "idiota/master/mais/master"
    region = "sa-east-1"
  }
}