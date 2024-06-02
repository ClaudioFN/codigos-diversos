"""
Created Date: 30/05/2023
Last Update: 30/05/2023
Description: Small bank operations
Observation: Using a bank system to operate details of a bank account like account statement, deposit and withdraw.
"""
class Main:
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    
    def __call__(self):
        pass
    
    def bank_deposit(self, deposit_value):
        if deposit_value > 0:
            self.saldo += deposit_value
            print(f'Account now have R${self.saldo:.2f}')
        else:
            print(f'Value to deposit is invalid: R${deposit_value}')

    def bank_withdraw(self, withdraw_value):
        if (self.saldo - withdraw_value) > 0:
            if (self.numero_saques > self.LIMITE_SAQUES):
                self.saldo -= withdraw_value
                self.numero_saques += 1
                print(f'Account now have R${self.saldo:.2f}')
            else:
                print(f'Withdraw limit for the day reached.')
        else:
            print(f'The account doesn\'t have enough value to withdraw. Current value in the account: R${self.saldo:.2f}')
    
    def bank_account_statement(self):
        account_statement = f'''
                Welcome to PBank!
        Your account has R${self.saldo:.2f}
        '''
        print(account_statement)
        
    def bank_menu(self):
        while True:
            option = input(f"Select the option: {self.menu}")
            
            if option == 'd':
                print('Deposit Operation Selected\n')
                value_deposit = float(input('Please type the value to deposit: '))
                self.bank_deposit(self, value_deposit)
            elif option == 's':
                print('Withdraw Operation Selected\n')
                value_withdraw = float(input('Please type the value to withdraw: '))
                self.bank_withdraw(self, value_withdraw)
            elif option == 'e':
                print('Account Statement Operation Selected\n')
                self.bank_account_statement(self)
            elif option == 'q':
                print('Sair')
                break
            else:
                print('Invalid Option! Select again.\n')

o = Main 
o.bank_menu(self=Main)