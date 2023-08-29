from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    """
    Abstract model providing common fields for auditing and tracking changes.

    Fields:
        created_on (DateTimeField, nullable): The timestamp when the model instance was created.
        created_by (ForeignKey to User, nullable): The user who created the model instance.
        updated_on (DateTimeField, nullable): The timestamp when the model instance was last updated.
        updated_by (ForeignKey to User, nullable): The user who last updated the model instance.
        deleted_on (DateTimeField, nullable): The timestamp when the model instance was soft-deleted.
        deleted_by (ForeignKey to User, nullable): The user who soft-deleted the model instance.
        is_deleted (BooleanField): Indicates if the model instance is soft-deleted (True) or active (False).

    Meta:
        abstract = True

    Usage:
        The BaseModel is designed to be used as a parent or mixin class for other models that require
        auditing and change tracking features. By inheriting from the BaseModel, child models automatically
        gain the common fields to track creation, update, and soft deletion of records.

    Example Usage:
        # Creating a child model that inherits from BaseModel
        class MyModel(BaseModel):
            # Additional fields and methods specific to MyModel...
    """

    created_on = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+')
    updated_on = models.DateTimeField(null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+')
    deleted_on = models.DateTimeField(null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
