from shadowd.django_connector import InputDjango, OutputDjango, Connector

class ShadowdConnectorMiddleware(object):
    def process_request(self, request):
        input = InputDjango(request)
        output = OutputDjango()

        status = Connector().start(input, output)
        if not status == True:
            return status
