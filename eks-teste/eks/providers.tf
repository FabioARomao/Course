terraform {
  backend "s3" {
    bucket = "romao-eks-teste"
    key    = "romao-eks-vaila"
    region = "sa-east-1"
  }
}
