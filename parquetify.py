from s3_parquetifier import S3Parquetifier

# Call the covertor
S3Parquetifier(
    source_bucket="aws-uggr-demo",
    target_bucket="aws-uggr-demo",
    verbose=True,  # for verbosity or not
).convert_from_s3(
    source_key="titanic.csv",
    target_key="parquet/data/",
    chunk_size=100  # The number of rows per parquet
)