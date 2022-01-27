terraform {
  backend "s3" {
    bucket = "romaoeksdeteste"
    key    = "romaoeksdeteste/for/my/eks"
    region = "sa-east-1"
  }
}
