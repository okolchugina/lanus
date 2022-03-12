import logging
from importlib import import_module

import bluetooth

log = logging.getLogger(__name__)


class BTServer:

    socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    @property
    def config(self):
        return import_module('config.lotus')

    def bind(self):
        self.socket.bind(getattr(self.config, 'PORT', 1))

    def listen(self):
        self.socket.listen(1)

    def run(self):
        self.bind()

        while True:
            self.listen()
            client, (ip, port) = self.socket.accept()
            log.info(f'connected client: {ip}:{port}')

            try:
                #TODO заменить на работу с приложением
                data = client.recv(1024)
                print("received [%s]" % data)

                client.send('success')
            except Exception as e:
                log.error(e)
                break

        self.socket.close()


