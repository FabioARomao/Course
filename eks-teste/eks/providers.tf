terraform {
  backend "s3" {
    bucket = "romaoekssaeast"
    key    = "romaoeksdeteste/for/my/eks"
    region = "sa-east-1"
  }
}
