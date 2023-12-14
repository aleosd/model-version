# Model version

**Model version** allows to track changes to Django model instances. Each time
an instance is updated, its `version` number is incremented and old values are
copied to a new record, that represents previous version of the current instance.

## Installation

To install the library use pip:

```shell
pip install model_version
```

## Usage

To enable model versioning `ModelVersion` should be used as one of base classes
a model inherits from:

```python
from model_version import ModelVersion


class MyModel(ModelVersion):
    ...
```

This will add three new fields to the model:

* `version` - integer number starting from `0` (default version start number)
* `version_id` - `uuid4` that represents different versions of the same record
* `version_created_at` - timestamp record

Create and apply migrations with the new fields:

```shell
python ./manage.py makemigration
python ./manage.py migrate
```

## Limitations

1. Doesn't work with bulk operations.
2. Requires additional DB query on save.
