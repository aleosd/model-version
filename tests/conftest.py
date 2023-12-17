import pytest
from myapp.models import MyModel


@pytest.mark.django_db
@pytest.fixture()
def model_instance() -> MyModel:
    yield MyModel.objects.create(name="foo")
