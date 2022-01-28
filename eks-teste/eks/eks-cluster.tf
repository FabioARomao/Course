module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  cluster_name    = local.cluster_name
  cluster_version = "1.21"
  tags = {
    Environment = "testando"
    GithubRepo  = "terraform-aws-eksone"
    GithubOrg   = "terraform-aws-modules"
  }

  vpc_id  = module.vpc.vpc_id
  subnet_ids = module.vpc.public_subnets

  # Self Managed Node Group(s)
  self_managed_node_group_defaults = {
    instance_type                          = "t2.micro"
    update_launch_template_default_version = true
    #iam_role_additional_policies           = ["arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"]
  }

  self_managed_node_groups = {
    one = {
      name = "spot-1"

      public_ip    = true
      max_size     = 2
      desired_size = 2

      use_mixed_instances_policy = true
      mixed_instances_policy = {
        instances_distribution = {
          on_demand_base_capacity                  = 0
          on_demand_percentage_above_base_capacity = 10
          spot_allocation_strategy                 = "capacity-optimized"
        }

        override = [
          {
            instance_type     = "t2.micro"
            weighted_capacity = "1"
          },
          {
            instance_type     = "t2.small"
            weighted_capacity = "2"
          },
        ]
      }
    }
  }

  #workers_group_defaults = {
  #  root_volume_type = "gp2"
  #}

#  worker_groups = [
#    {
#      name                          = "worker-group-1"
#      instance_type                 = "t2.micro"
#      additional_userdata           = "echo foo bar"
#      asg_desired_capacity          = 1
#      additional_security_group_ids = [aws_security_group.worker_group_mgmt_one.id]
#    },
#    {
#      name                          = "worker-group-2"
#      instance_type                 = "t2.micro"
#      additional_userdata           = "echo foo bar"
#      additional_security_group_ids = [aws_security_group.worker_group_mgmt_two.id]
#      asg_desired_capacity          = 1
#    },
#  ]
}

data "aws_eks_cluster" "cluster" {
  name = module.eks.cluster_id
}

data "aws_eks_cluster_auth" "cluster" {
  name = module.eks.cluster_id
}

provider "kubernetes" {
  host                   = data.aws_eks_cluster.cluster.endpoint
  cluster_ca_certificate = base64decode(data.aws_eks_cluster.cluster.certificate_authority.0.data)
  token                  = data.aws_eks_cluster_auth.cluster.token
}