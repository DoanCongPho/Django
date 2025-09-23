from django.contrib import admin
from .models import Conversation, Participant, User


class ParticipantInline(admin.TabularInline): 
    model = Participant
    extra = 0
    fields = ("conversation", "role", "join_at")
    readonly_fields = ("join_at",)


class ConversationAdmin(admin.ModelAdmin): 
    fieldsets = [
        (None, {"fields": ["name", "type"]}),
        ("Timestamps", {"fields": ["created_at"]}),
    ]
    readonly_fields = ("created_at",)
    inlines = [ParticipantInline]


class UserAdmin(admin.ModelAdmin): 
    fieldsets = [
        (None, {"fields": ["name"]}),
        ("Timestamps", {"fields": ["created_at"]}),
    ]
    readonly_fields = ("created_at",)
    inlines = [ParticipantInline]


admin.site.register(User, UserAdmin)
admin.site.register(Participant)
admin.site.register(Conversation, ConversationAdmin)
