from storages.backends.s3boto3 import S3BotoStorage

class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False