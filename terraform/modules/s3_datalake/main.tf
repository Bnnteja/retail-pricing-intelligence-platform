resource "aws_s3_bucket" "this" {
  bucket = var.bucket_name

  tags = var.tags
}

resource "aws_s3_bucket_versioning" "this" {
  bucket = aws_s3_bucket.this.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "this" {
  bucket = aws_s3_bucket.this.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_object" "folders" {
  for_each = toset([
    "raw/",
    "raw/pos_transactions/",
    "raw/fuel_prices/",
    "raw/products/",
    "raw/stores/",
    "processed/",
    "processed/processed_transactions/",
    "processed/category_sales_summary/",
    "processed/fuel_margin_analysis/",
    "processed/pricing_recommendations/",
    "curated/",
    "athena-results/"
  ])

  bucket  = aws_s3_bucket.this.id
  key     = each.value
  content = ""

  tags = var.tags
}
