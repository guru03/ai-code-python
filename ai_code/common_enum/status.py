from enum import Enum


class WorkStatus(Enum):
    Pending = "pending"
    Draft = "draft"
    InReview = "in review"
    Approved = "approved"
    Rejected = "rejected"
    Updated = "updated"
    Archived = "archived"
    Completed = "completed"
    InProgress = "in progress"


class WorkStatusInProgress(Enum):
    Draft = "draft"
    InReview = "in review"
    Approved = "approved"
    Rejected = "rejected"
    Archived = "archived"
    Completed = "completed"
    InProgress = "in progress"


#! Not in use, but can be used for future reference
STATUS_CHOICES = [
    ("pending", "Pending"),
    ("approved", "Approved"),
    ("rejected", "Rejected"),
    ("updated", "Updated"),
    ("archived", "Archived"),
]