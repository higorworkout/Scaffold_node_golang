# output "example_output" {
#   value = aws_s3_bucket.example.id
# }

output "db_endpoint" {
  value = module.rds.db_endpoint
}

output "ecs_cluster_name" {
  value = module.ecs.cluster_name
}