provider "aws" {
    region = "${var.AWS_REGION}"
    profile = "${var.AWS_PROFILE}" # lets say profile is my-profile
}