terraform {
  backend "s3" {
    encrypt                 = true
    bucket                  = "romaos3-backend-eks"
    dynamodb_table          = "romaos3table-state-lock-dynamo"
    region                  = "sa-east-1"
    workspace_key_prefix    = "testing"
    key                     = "eks/terraform.tfstate"
    profile                 = "novachave"
    shared_credentials_file = "~/.aws/credentials"
  }
}
