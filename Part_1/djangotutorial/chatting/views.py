from django.http import HttpResponse
from django.views import generic
from .models import * 
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = "chatting/index.html"
    context_object_name = "conversations"
    model = Conversation 

class ConversationView(LoginRequiredMixin, generic.DetailView): 
    model = Conversation
    template_name = "chatting/conversation.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs) 
        conversation = self.get_object() 

        context["participants"] = conversation.participants.all() 
        context["messages"] = conversation.messages.order_by("-created_at")[:10]


        return context
    
    