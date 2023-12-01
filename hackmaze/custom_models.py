from model_utils.models import TimeStampedModel, UUIDModel


class AbstractModel(TimeStampedModel, UUIDModel):
    ...
