from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def send_booking_confirmation(user_email, booking, reservation):
    subject = "🎟️ Your Ticket Booking Confirmation"
    
    html_message = render_to_string('bookings/email_ticket.html', {
        'booking': booking,
        'reservation': reservation,
        'user_email': user_email,
    })
    
    plain_message = strip_tags(html_message)

    send_mail(
        subject,
        plain_message,
        settings.EMAIL_HOST_USER,
        [user_email],
        html_message=html_message,
    )