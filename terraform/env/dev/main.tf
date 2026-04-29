locals {
  tags = {
    Project = var.project
    Env     = var.env
    Owner   = var.owner
  }
}

module "s3_datalake" {
  source = "../../modules/s3_datalake"

  bucket_name = var.bucket_name
  tags        = local.tags
}

module "glue_catalog" {
  source = "../../modules/glue_catalog"

  database_name = var.glue_database_name
  tags          = local.tags
}
