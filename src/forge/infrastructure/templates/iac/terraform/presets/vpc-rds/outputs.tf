# output "example_output" {
#   value = aws_s3_bucket.example.id
# }

output "vpc_id" {
  value = module.vpc.vpc_id
}

output "db_endpoint" {
  value = module.rds.db_endpoint
}