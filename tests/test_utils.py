from contextvars import Token

from hamcrest import assert_that, instance_of, is_, not_none

from model_version.settings import versioning_is_disabled
from model_version.utils import disabled_versioning


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
