import pytest
from hamcrest import assert_that, equal_to, less_than, not_
from myapp.models import MyModel

from model_version.settings import DEFAULT_VERSION


@pytest.mark.django_db
@pytest.fixture()
def model_instance() -> MyModel:
    yield MyModel.objects.create(name="foo")


@pytest.mark.django_db
def test__default_version_when_new_record_created(model_instance):
    assert_that(model_instance.version, equal_to(DEFAULT_VERSION))


@pytest.mark.django_db
def test__version_updated_on_save(model_instance):
    # when
    model_instance.name = "bar"
    model_instance.save()

    # then
    assert_that(model_instance.version, equal_to(DEFAULT_VERSION + 1))


@pytest.mark.django_db
def test__new_record_created_on_save(model_instance):
    # when
    model_instance.name = "bar"
    model_instance.save()

    # then
    assert_that(MyModel.objects.count(), equal_to(2))


@pytest.mark.django_db
def test__old_record_retains_old_data(model_instance):
    # when
    old_name = model_instance.name
    old_version = model_instance.version
    old_version_created_at = model_instance.version_created_at
    model_instance.name = "bar"
    model_instance.save()

    # then
    old_record = MyModel.objects.exclude(pk=model_instance.pk).first()
    assert_that(old_record.name, equal_to(old_name))
    assert_that(old_record.version, equal_to(old_version))
    assert_that(old_record.version_created_at, equal_to(old_version_created_at))
    assert_that(old_record.version_created_at, not_(equal_to(model_instance.version_created_at)))
    assert_that(old_record.version_created_at, less_than(model_instance.version_created_at))
    assert_that(old_record.version_id, equal_to(model_instance.version_id))


@pytest.mark.django_db
def test__new_version_is_based_on_latest(model_instance):
    # when
    model_instance.name = "bar"
    model_instance.save()
    old_record = MyModel.objects.exclude(pk=model_instance.pk).first()
    old_record.name = "baz"
    old_record.save()

    # then
    assert_that(MyModel.objects.count(), equal_to(3))
    first_record = MyModel.objects.get(name="foo")
    second_record = MyModel.objects.get(name="bar")
    third_record = MyModel.objects.get(name="baz")
    assert_that(first_record.version, equal_to(0))
    assert_that(second_record.version, equal_to(1))
    assert_that(third_record.version, equal_to(2))


@pytest.mark.django_db
def test__different_record_have_different_version_id():
    # when
    first_record = MyModel.objects.create(name="foo")
    second_record = MyModel.objects.create(name="bar")

    # then
    assert_that(first_record.version_id, not_(equal_to(second_record.version_id)))
