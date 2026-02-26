variable "project_name" { type = string }
variable "vpc_id" { type = string }
variable "public_subnet_id" { type = string }

variable "container_image" { type = string }
variable "container_port" { type = number }
variable "target_group_arn" { type = string }
