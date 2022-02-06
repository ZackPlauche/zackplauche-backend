from django.db.models import TextChoices


class ProjectRole(TextChoices):
    OWNER = 'Owner'
    COLLABORATOR = 'Collaborator'
    PARTNER = 'Partner'
    LEAD_DEVELOPER = 'Lead Developer'


class ProjectStatus(TextChoices):
    PROTOTYPE = 'Prototype'
    LIVE = 'Live'
    COMPLETED = 'Completed'
    IN_PROGRESS = 'In Progress'
    PAUSED = 'Paused'
    CONCEPT = 'Concept'
