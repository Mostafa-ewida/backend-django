from model_utils.models import TimeStampedModel, UUIDModel


class AbstractCoreModel(TimeStampedModel, UUIDModel):
    class Meta:
        abstract = True
