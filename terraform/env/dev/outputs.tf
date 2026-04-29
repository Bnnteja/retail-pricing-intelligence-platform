output "s3_bucket_name" {
  value = module.s3_datalake.bucket_name
}

output "glue_database_name" {
  value = module.glue_catalog.database_name
}

output "athena_results_path" {
  value = "s3://${module.s3_datalake.bucket_name}/athena-results/"
}
