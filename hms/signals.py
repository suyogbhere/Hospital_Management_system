from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from hms.models import User, Patient,Doctor,Staff

'''When user register that time it reflect in respective table'''
@receiver(post_save, sender=User)
def create_related_profile(sender, instance, created, **kwargs):
    if created:
        # Create Patient profile if is_patient is True
        if instance.is_patient:
            Patient.objects.create(user=instance)

        if instance.is_staff:
            Staff.objects.create(user=instance)

        if instance.is_doctor:
            Doctor.objects.create(user=instance)
        
@receiver(pre_save, sender=User)
def ensure_is_patient(sender, instance, **kwargs):
    print(f"Before save: {instance.is_patient}")

@receiver(pre_save, sender=User)
def ensure_is_staff(sender, instance, **kwargs):
    print(f"Before save: {instance.is_staff}")

@receiver(pre_save, sender=User)
def ensure_is_doctor(sender, instance, **kwargs):
    print(f"Before save: {instance.is_doctor}")


'''When admin user assign specific user to patient or staff or doctor from 
admin panel then it reflect data to respective table'''
@receiver(post_save, sender=User)
def create_patient_if_needed(sender, instance, **kwargs):
    if instance.is_patient :               #Assuming is_patient is custom field in your User model
        Patient.objects.get_or_create(user=instance)
    else:
        '''Optional : remove the patient record if "is_patient" is set to False'''
        Patient.objects.filter(user=instance).delete()

@receiver(post_save, sender=User)
def create_staff_if_needed(sender, instance, **kwargs):
    if instance.is_staff :               #Assuming is_patient is custom field in your User model
        Staff.objects.get_or_create(user=instance)
    else:
        '''Optional : remove the patient record if "is_patient" is set to False'''
        Staff.objects.filter(user=instance).delete()

@receiver(post_save, sender=User)
def create_doctor_if_needed(sender, instance, **kwargs):
    if instance.is_doctor :               #Assuming is_patient is custom field in your User model
        Doctor.objects.get_or_create(user=instance)
    else:
        '''Optional : remove the patient record if "is_patient" is set to False'''
        Doctor.objects.filter(user=instance).delete()

