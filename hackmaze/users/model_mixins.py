from model_utils.models import TimeStampedModel, UUIDModel


class UserMixin(TimeStampedModel, UUIDModel):
    ...
