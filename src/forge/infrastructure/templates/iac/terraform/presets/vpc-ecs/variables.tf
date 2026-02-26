variable "project_name" { type = string }

variable "cidr_block" {
  type    = string
  default = "10.0.0.0/16"
}

variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "db_username" {
  type    = string
  default = "postgres"
}

variable "db_password" {
  type      = string
  sensitive = true
}

variable "container_image" {
  type    = string
  default = "nginx"
}

variable "container_port" {
  type    = number
  default = 80
}
