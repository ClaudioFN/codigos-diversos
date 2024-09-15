import re
class Documento:
    def valida_documento(documento):

        documento = re.sub(r'[./-]', "", documento) # Substitui os caracteres '.', '/' e '-' por strings vazias ("").

        if len(documento) == 11:
            if re.match(r"[0-9]{11}", documento):
                return True
            else:
                return False
        elif len(documento) == 14:
            if re.match(r"[0-9]{14}", documento):
                return True
            else:
                return False
        else:
            raise print('Quantidade de dígitos está incorreta!!')


