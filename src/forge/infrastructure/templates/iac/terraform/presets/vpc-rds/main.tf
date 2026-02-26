# Exemplo de recurso inicial
# resource "aws_s3_bucket" "example" {
#   bucket = "${var.project_name}-bucket"
# }


module "vpc" {
  source = "./modules/vpc"

  project_name = var.project_name
  cidr_block   = var.cidr_block
}

module "rds" {
  source = "./modules/rds"

  project_name      = var.project_name
  vpc_id            = module.vpc.vpc_id
  private_subnet_id = module.vpc.private_subnet_id
  db_username       = var.db_username
  db_password       = var.db_password
}