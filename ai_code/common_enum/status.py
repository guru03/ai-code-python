from enum import Enum


class WorkStatus(Enum):
    Draft = "draft"
    InReview = "in_review"
    Approved = "approved"
    Rejected = "rejected"
    Archived = "archived"
    Completed = "completed"
    InProgress = "in_progress"
