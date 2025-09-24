from django.db import models
from django.utils.translation import gettext_lazy as _


class User(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)

    def __str__(self):
        return self.name


class Conversation(models.Model):
    name = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    type = models.CharField(max_length=50, choices = [("Direct", "direct"), ("Group", "group")], null=True, blank=True) 
    participants = models.ManyToManyField(
        "User",
        through="Participant",
        related_name="conversations"
    )
    def __str__(self):
        if self.type.lower() == "group":
            return self.name
        names = [p.name for p in self.participants.all()]
        return "&".join(names)

class Participant(models.Model):
    conversation = models.ForeignKey(
        Conversation, on_delete=models.CASCADE, related_name="participant_links"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="participant_links"
    )

    role = models.CharField(
        max_length=10,
        choices=[("admin", "Admin"), ("member", "Member")],blank=True
    )
    join_at = models.DateTimeField(_("Join at"), auto_now_add=True)
    nickname = models.CharField(max_length=30, blank=True, null=True) 

    class Meta:
        unique_together = ("conversation", "user")  

    def __str__(self):
        if self.conversation.type and self.conversation.type.lower() == "group":
            return f"{self.user.name} in {self.conversation.name} as {self.role or 'member'}"
        
        others = self.conversation.participants.exclude(id=self.user.id)
        if others.exists():
            return f"{self.user.name} ↔ {others.first().name}"
        return f"{self.user.name} (alone in direct chat)"

class Message(models.Model): 
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  


    def __str__(self):
        return f"{self.sender.name}: {self.content[:30]}"
     
    