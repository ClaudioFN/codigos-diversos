"""
Created Date: 30/05/2023
Last Update: 15/06/2023
Description: Small bank operations
Observation: Using a bank system to operate details of a bank account like account statement, deposit and withdraw.
"""
import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Client:
    def __init__(self, address):
        self.address = address
        self.accounts = []
        self.account_index = 0

    def make_transaction(self, account, transaction):
        transaction.register(account)

    def add_count(self, account):
        self.accounts.append(account)


class PessoaFisica(Client):
    def __init__(self, name, birth_date, cpf, address):
        super().__init__(address)
        self.name = name
        self.birth_date = birth_date
        self.cpf = cpf


class Account:
    def __init__(self, client_number, client):
        self._balance = 0
        self._client_number = client_number
        self._agency = "0001"
        self._client = client
        self._history = History()

    @classmethod
    def new_account(cls, client, client_number):
        return cls(client_number, client)

    @property
    def balance(self):
        return self._balance

    @property
    def client_number(self):
        return self._client_number

    @property
    def agency(self):
        return self._agency

    @property
    def client(self):
        return self._client

    @property
    def history(self):
        return self._history

    def withdraw(self, valor):
        balance = self.balance
        excedeu_balance = valor > balance

        if excedeu_balance:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._balance -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def deposit(self, valor):
        if valor > 0:
            self._balance += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True


class AccountCorrente(Account):
    def __init__(self, client_number, client, limit=500, limit_withdraw=3):
        super().__init__(client_number, client)
        self._limit = limit
        self._limit_withdraw = limit_withdraw

    def withdraw(self, valor):
        client_number_withdraw = len(
            [transaction for transaction in self.history.transacoes if transaction["type"] == Withdraw.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_withdraw = client_number_withdraw >= self._limite_withdraw

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_withdraw:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().withdraw(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agency}
            C/C:\t\t{self.client_number}
            Titular:\t{self.client.name}
        """

class History:
    def __init__(self):
        self._transactions = []

    @property
    def transactions(self):
        return self._transactions

    def add_transaction(self, transaction):
        self._transactions.append(
            {
                "type": transaction.__class__.__name__,
                "value": transaction.valor,
                "date": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )
        
    #def generate_report(self, type_transaction=None):
    #    for transaction in self._transacoes:
    #        if (
    #            type_transaction is None
    #            or transaction["type"].lower() == type_transaction.lower()
    #        ):
    #            yield transaction

    #def transactions_of_day(self):
    #    actual_date = datetime.utcnow().date()
    #    transactions = []
    #    for transaction in self._transactions:
    #        date_transaction = datetime.strptime(
    #            transaction["date"], "%d-%m-%Y %H:%M:%S"
    #        ).date()
    #        if actual_date == date_transaction:
    #            transactions.append(transaction)
    #    return transactions

class Transaction(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def register(self, account):
        pass


class Withdraw(Transaction):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def register(self, account):
        success_transaction = account.withdraw(self.valor)

        if success_transaction:
            account.history.add_transaction(self)


class Deposit(Transaction):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def register(self, account):
        success_transaction = account.depositar(self.valor)

        if success_transaction:
            account.history.add_transaction(self)

    #def log_transaction(func):
    #    def envelope(*args, **kwargs):
    #        result = func(*args, **kwargs)
    #        print(f"{datetime.now()}: {func.__name__.upper()}")
    #        return result
    #
    #    return envelope

class Main:
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """

    balance = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    
    def __call__(self):
        pass

    def filter_client(cpf, clients):
        client_filtred = [client for client in clients if client.cpf == cpf]
        return client_filtred[0] if client_filtred else None

    def retrieve_client_account(client):
        if not client.accounts:
            print("\n@@@ Cliente não possui conta! @@@")
            return

        return client.accounts[0]

    def deposit(clients):
        cpf = input("Informe o CPF do cliente: ")
        client = Main.filter_client(cpf, clients)

        if not client:
            print("\n@@@ Cliente não encontrado! @@@")
            return

        value = float(input("Informe o valor do depósito: "))
        transaction = Deposit(value)

        account = Main.retrieve_client_account(client)
        if not account:
            return

        client.make_transaction(account, transaction)

    #@log_transaction
    def withdraw(clients):
        cpf = input("Informe o CPF do cliente: ")
        client = Main.filter_client(cpf, clients)

        if not client:
            print("\n@@@ Cliente não encontrado! @@@")
            return

        value = float(input("Informe o valor do saque: "))
        transaction = Withdraw(value)

        account = Main.retrieve_client_account(client)
        if not account:
            return

        client.make_transaction(account, transaction)

    #@log_transaction
    def show_extrato(clients):
        cpf = input("Informe o CPF do cliente: ")
        client = Main.filter_client(cpf, clients)

        if not client:
            print("\n@@@ Cliente não encontrado! @@@")
            return

        account = Main.retrieve_client_account(client)
        if not account:
            return

        print("\n================ EXTRATO ================")
        transactions = account.history.transaction

        extrato = ""
        if not transactions:
            extrato = "Não foram realizadas movimentações."
        else:
            for transaction in transactions:
                extrato += f"\n{transaction['tipo']}:\n\tR$ {transaction['valor']:.2f}"

        print(extrato)
        print(f"\nSaldo:\n\tR$ {account.balance:.2f}")
        print("==========================================")

    #@log_transaction
    def create_client(clients):
        cpf = input("Informe o CPF (somente número): ")
        client = Main.filter_client(cpf, clients)

        if client:
            print("\n@@@ Já existe cliente com esse CPF! @@@")
            return

        name = input("Informe o nome completo: ")
        birth_date = input("Informe a data de nascimento (dd-mm-aaaa): ")
        address = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        client = PessoaFisica(name=name, birth_date=birth_date, cpf=cpf, address=address)

        clients.append(client)

        print("\n=== Cliente criado com sucesso! ===")

    #@log_transaction
    def create_account(account_number, clients, accounts):
        cpf = input("Informe o CPF do cliente: ")
        client = Main.filter_client(cpf, clients)

        if not client:
            print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
            return

        account = AccountCorrente.new_account(client=client, client_number=account_number)
        accounts.append(account)
        client.accounts.append(account)

        print("\n=== Conta criada com sucesso! ===")


    def list_accounts(accounts):
        for account in accounts:
            print("=" * 100)
            print(textwrap.dedent(str(account)))
    
    # TODO: AQUI MENU TROCAR
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