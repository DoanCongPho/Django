from django.db import models
from django.utils.translation import gettext_lazy as _


class User(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)

    def __str__(self):
        return self.name


class Conversation(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    type = models.CharField(max_length=50, choices = [("Direct", "direct"), ("Group", "group")], null=True, blank=True) 
    participants = models.ManyToManyField(
        "User",
        through="Participant",
        related_name="conversations"
    )
    def __str__(self):
        return self.name


class Participant(models.Model):
    conversation = models.ForeignKey(
        Conversation, on_delete=models.CASCADE, related_name="participant_links"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="participant_links"
    )

    role = models.CharField(
        max_length=10,
        choices=[("admin", "Admin"), ("member", "Member")]
    )
    join_at = models.DateTimeField(_("Join at"), auto_now_add=True)
    nickname = models.CharField(max_length=30, blank=True, null=True) 

    class Meta:
        unique_together = ("conversation", "user")  

    def __str__(self):
        return f"{self.user.name} in {self.conversation.name} as {self.role}"