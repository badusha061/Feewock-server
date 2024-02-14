from .serializer import CardInformationSerializer 
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
import stripe
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework import status
from rest_framework import status
from rest_framework.views import APIView
import logging
from django.shortcuts import redirect
from booking.models import Appointment
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
stripe.api_key = settings.STRIPE_SECRET_KEY



@permission_classes([IsAuthenticated])
class StripeCheckoutView(APIView):
    def post(self, request ,*args, **kwargs):
        appoitment_instane = Appointment.objects.get(id = self.kwargs['pk'])
        try:
            app_id = self.kwargs['pk']
            customer = stripe.Customer.create(
                name=appoitment_instane.user.first_name,
                address={
                    'line1': appoitment_instane.user.location,
                    'city':  appoitment_instane.user.location,
                    'postal_code': '123232',
                    'country': 'DK',
                }
            )
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=[
                    {
                        "price_data":{
                            'unit_amount': int(appoitment_instane.service_amount * 100),
                            'currency':'INR',
                            "product_data" :{
                                'name': f"Hy {appoitment_instane.name} Your service Amount"
                            }
                        },
                        'quantity': 1,
                    },
                ],  
                mode='payment',
                success_url=settings.SITE_URL + f'/?success=true&session_id={{CHECKOUT_SESSION_ID}}&appointment_id={app_id}',
                cancel_url=settings.SITE_URL + '/?canceled=true',
                customer=customer.id
            )
            return Response({"message":checkout_session})
        except Exception as e :
            print(e)
            return Response(
                {'error': 'Something went wrong when creating stripe checkout session'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

