import datetime
from random import randint
class verify:

    @property
    def create_verify_code(self):
        created_verify_code = str(randint(100000, 999999))
        return created_verify_code

    @property
    def check_verify_code(self, created_code, verify_code):
        '''check the verify code with inputed code if
            the expiry date is not over
        
        '''
        pass

