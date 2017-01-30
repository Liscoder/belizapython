import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEYs') or 'SECRET_KEY'
	PAGE_ACCESS_TOKEN = os.environ.get('PAGE_ACCESS_TOKEN') or 'EAANXVZBnHyLMBAILPZA6oR79uuRv7HIJgjLen7JQXuNEJdNVwGvtaLHeFh3CTAQp2UwtOwPOcry57uu4McAnPmvAqylgBvRHnCXNt31aG2T7LVu30hCOZB2clw1YXM2OP76TIYmoS8X7fjUL4k48xLYZBmuR5BLYQkaRaxV2LAZDZD'
	USER_GEONAMES = os.environ.get('USER_GEONAMES')
class DevelopmentConfig(Config):
	DEBUG = True
