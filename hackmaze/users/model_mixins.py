from model_utils.models import SoftDeletableModel, TimeStampedModel, UUIDModel


class UserMixin(TimeStampedModel, UUIDModel, SoftDeletableModel):
    ...
