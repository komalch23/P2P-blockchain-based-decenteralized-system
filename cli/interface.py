import cmd

from cli.command import Command


class Interface(cmd.Cmd):

    def __init__(self):
        super().__init__()
        self.prompt = '(blockchain) '
        self._default_host = '127.0.0.1'
        self._command = Command()

    def do_open(self, port):
        '''
        Open peer listening port Eg: open 5000
        '''
        self._command.start_peer(self._default_host, int(port))

    def do_mine(self, arg):
        '''
        Mine a new block Eg: mine hello
        '''
        port = arg.split(' ')[0]
        data = arg.split(' ')[1]
        self._command.mine(self._default_host, int(port), data)

    def do_connect(self, arg):
        '''
        Connect a peer to another Eg: connect 5000 5001
        '''
        port = arg.split(' ')[0]
        target_port = arg.split(' ')[1]
        self._command.connect_peer(
            self._default_host, int(port), self._default_host, int(target_port))

    def do_show(self, port):
        '''
        Show blockchain of peer Eg: show 5000
        '''
        self._command.get_chain(self._default_host, int(port))

    def do_exit(self, _):
        exit(0)

    def do_help(self, _):
        print('\n')
        print('Commands:')
        print('\n')
        print('Type: "help" \t\t\t\t to get help with commands')
        print('Type: "exit" \t\t\t\t to exit application')
        print('\n')
        print('Type: "open <your port>" \t\t\t to open peer listening port Eg: open 5000')
        print(
            'Type: "connect <your port> <your_target_port>" \t '
            'to connect a peer to another Eg: connect 5000 6000')
        print('\n')
        print('Type: "mine <port> <data>" \t\t to mine a new block Eg: mine 5000 hello')
        print('Type: "show <port> \t\t\t" to show a blockchain of peer/s Eg: show 5000')
        print('\n')
