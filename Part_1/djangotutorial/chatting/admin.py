from django.contrib import admin
from .models import Conversation, Participant, User, Message


class ParticipantInline(admin.TabularInline): 
    model = Participant
    extra = 0
    fields = ("user","conversation", "role", "join_at",)
    readonly_fields = ("join_at",)

class MessageInline(admin.TabularInline):
    model = Message
    extra = 1
    fields = ("sender","content", "created_at",)
    readonly_fields = ("created_at",)
 


class ConversationAdmin(admin.ModelAdmin): 
    fieldsets = [
        (None, {"fields": ["name", "type"]}),
        ("Timestamps", {"fields": ["created_at"]}),
    ]
    readonly_fields = ("created_at",)
    inlines = [ParticipantInline, MessageInline]



class UserAdmin(admin.ModelAdmin): 
    fieldsets = [
        (None, {"fields": ["name"]}),
        ("Timestamps", {"fields": ["created_at"]}),
    ]
    readonly_fields = ("created_at",)
   

class ParticipantAdmin(admin.ModelAdmin): 
    fieldsets = [
        (None, {"fields": ["conversation"]}), 
        (None, {"fields": ["user"]}), 
        (None, {"fields": ["role"]}), 
        (None, {"fields": ["nickname"]})
    ] 



admin.site.register(User, UserAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Conversation, ConversationAdmin)
