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

module "ecs" {
  source = "./modules/ecs"

  project_name       = var.project_name
  vpc_id             = module.vpc.vpc_id
  public_subnet_id   = module.vpc.public_subnet_id
  container_image    = var.container_image
  container_port     = var.container_port
}