from contextvars import Token
from hamcrest import assert_that, is_, is_not, not_none, instance_of
from model_version.utils import disabled_versioning
from model_version.constants import versioning_is_disabled


def test__disabled_versioning_context__changes_context_variable():
    # given
    reset_token = versioning_is_disabled.set(False)

    # when
    with disabled_versioning() as ctx:
        assert_that(ctx._context_token, not_none())
        assert_that(ctx._context_token, instance_of(Token))
        assert_that(versioning_is_disabled.get(), is_(True))

    # then
    assert_that(versioning_is_disabled.get(), is_(False))
    versioning_is_disabled.reset(reset_token)
