from storages.backends.s3boto3 import S3Boto3Storage

class TestS3MediaStorage(S3Boto3Storage):
    location = 'test-s3-upload/'
    default_acl = 'public-read'
    file_overwrite = False