import re
class Documento:
    def valida_documento(documento):

        documento = re.sub(r'[./-]', "", documento) # Changes the characters '.', '/' and '-' for empty strings ("").

        if len(documento) == 11: # Validates if the total amount of numbers is equal to the normal CPF quantity
            if re.match(r"[0-9]{11}", documento):
                return True
            else:
                return False
        elif len(documento) == 14: # Validates if the total amount of numbers is equal to the normal CNPJ quantity
            if re.match(r"[0-9]{14}", documento):
                return True
            else:
                return False
        else:
            raise print('Quantidade de dígitos está incorreta!')


