from abc import ABC, abstractmethod
class Account(ABC):
    @abstractmethod
    def download(self):
        pass

class PersonalAccount(Account):
    def download(self):
        print('Downloading the new app!')

class ProxyAccount(Account):
    def __init__(self, account: PersonalAccount, status='Guest'):
        self.account = account
        self.status = status
    def download(self):
        if self.status == 'Guest':
            print('You can not download the app by guest account.')
        else:
            self.account.download()

my_account = PersonalAccount()
new_account = ProxyAccount(my_account)

my_account.download()
new_account.download()
