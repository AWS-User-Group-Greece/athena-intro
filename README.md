# Install requirements
```
sudo apt-get install -y libssl-dev libffi-dev &&
sudo apt-get install -y libxml2-dev libxslt1-dev &&
sudo apt-get install -y libsnappy-dev
pip install -r requirements.txt
```

# Parquetify titanic.csv dataset
```
python parquetify.py
```

# Crawl the output results via [AWS Glue](https://eu-central-1.console.aws.amazon.com/glue/home?region=eu-central-1#catalog:tab=crawlers)

