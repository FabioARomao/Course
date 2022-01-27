terraform {
  backend "s3" {
    bucket = "romao-eks-teste"
    key    = "romao-eks-teste/key"
    region = "sa-east-1"
  }
}
