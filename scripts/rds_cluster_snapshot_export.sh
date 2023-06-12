#!/bin/bash
set -e
date=`date +'%Y-%m-%d'`
aurora_cluster_source_arn=`aws rds describe-db-cluster-snapshots --db-cluster-identifier $db_cluster_identifier --snapshot-type automated --query "DBClusterSnapshots[?SnapshotCreateTime>='$date'].DBClusterSnapshotArn" |  tr -d '"'| tr -d '[]' | tr -d ' '`
echo "Exporting Aurora Snapshot ($env_name) to S3"
aws rds start-export-task \
    --export-task-identifier ${env_name}-aurora-${date} \
    --source-arn $aurora_cluster_source_arn \
    --s3-bucket-name $s3_bucket \
    --iam-role-arn $iam_role \
    --kms-key-id $kms_key 
    