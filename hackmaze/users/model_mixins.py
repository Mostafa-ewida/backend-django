from model_utils.models import TimeStampedModel, UUIDModel


class UserProfileMixin(TimeStampedModel, UUIDModel):
    ...
