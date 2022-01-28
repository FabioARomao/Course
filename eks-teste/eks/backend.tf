terraform {
  backend "s3" {
    bucket = "romaoeks-eks-eks"
    key = "romaoeks-eks"
    region = "sa-east-1"
  }
}