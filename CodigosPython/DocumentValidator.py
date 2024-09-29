import re

# Document validator
class Document:
    def validate_document(document):

        document = re.sub(r'[./-]', "", document) # Changes the characters '.', '/' and '-' for empty strings ("").

        if len(document) == 11: # Validates if the total amount of numbers is equal to the normal CPF quantity
            if re.match(r"[0-9]{11}", document):
                return True
            else:
                return False
        elif len(document) == 14: # Validates if the total amount of numbers is equal to the normal CNPJ quantity
            if re.match(r"[0-9]{14}", document):
                return True
            else:
                return False
        else:
            raise print('Number of digits is invalid!')


