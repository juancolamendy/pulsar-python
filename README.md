# pulsar-python

## Install dependencies
```sh
pip install -r requirements.txt
```

## Run consumer
```sh
python consumer.py
```

## Run producer
```sh
python producer.py
```

# Get topic stats
```sh
curl http://localhost:8080/admin/v2/persistent/public/default/mytopic/stats | python -m json.tool
```
