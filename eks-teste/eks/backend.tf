terraform {
  backend "s3" {
    bucket = "romaoeks-eks-eks"
    key = "romaoeks-eks1"
    region = "sa-east-1"
  }
}
