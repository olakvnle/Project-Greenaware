from django.dispatch import receiver
from djoser import signals

@receiver(signals.activation_email_sent)
def disable_activation_email(sender, user, request, **kwargs):
    # Prevent the activation email from being sent
    # You can add your custom logic here if needed
    pass
