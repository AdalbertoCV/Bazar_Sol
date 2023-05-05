from django.core.validators import FileExtensionValidator, RegexValidator

matricula_validador_alumno = RegexValidator(
    regex='^[0-9]{8}$',
    message='La matrícula no tiene un formato válido (solo 8 digitos)',
    code='matricula_invalida'
)

matricula_validador_profesor = RegexValidator(
    regex='^[0-9]{10}$',
    message='La matrícula no tiene un formato válido (solo 10 digitos)',
    code='matricula_invalida'
)

curp_validador = RegexValidator(
    regex = '^([A-Z][AEIOUX][A-Z]{2}\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])[HM](?:AS|B[CS]|C[CLMSH]|D[FG]|G[TR]|HG|JC|M[CNS]|N[ETL]|OC|PL|Q[TR]|S[PLR]|T[CSL]|VZ|YN|ZS)[B-DF-HJ-NP-TV-Z]{3}[A-Z\d])(\d)$',
    message = 'CURP inválida.',
    code = 'curp_invalida'
)


imagen_validador = FileExtensionValidator(
    allowed_extensions=['png','jpg'],
    message="Sólo se permiten imágenes PNG"
)

rfc_validador = RegexValidator(
    regex='^([A-ZÑ&]{3,4}) ?(?:- ?)?(\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])) ?(?:- ?)?([A-Z\d]{2})([A\d])$',
    message='El RFC no tiene un formato válido',
    code='rfc_invalido'
)