from model_utils.models import SoftDeletableModel, TimeStampedModel, UUIDModel


class AbstractCoreModel(TimeStampedModel, UUIDModel, SoftDeletableModel):
    class Meta:
        abstract = True
