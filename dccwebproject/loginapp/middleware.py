from loginapp.models import User, Visitor
from django.contrib.sessions.models import Session

class OnlyOneUserMiddleware(object):
    def process_request(self, request):
         cur_session_key = request.user.visitor.session_key
         if cur_session_key and cur_session_key != request.session.session_key:
             Session.objects.get(session_key=cur_session_key).delete()
         #the following can be optimized(do not save each time if value not changed)
         request.user.visitor.session_key = request.session.session_key
         request.user.visitor.save()
