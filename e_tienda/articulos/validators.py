
from django.conf import settings
from django.core.validators import FileExtensionValidator
import os

image_validator = FileExtensionValidator(
    allowed_extensions = ['png', 'jpeg', 'jpg'], 
    message = "Sólo se permite formato PNG, JPEG, JPG.",
    code = 'formato_invalido'
)

def directory_path(instance, filename):
    banner_pic_name = 'articulos/img/{0}/{1}'.format(instance.nombre, filename)
    full_path = os.path.join(settings.MEDIA_ROOT, banner_pic_name)
    if os.path.exists(full_path):
        os.remove(full_path)
    return banner_pic_name
