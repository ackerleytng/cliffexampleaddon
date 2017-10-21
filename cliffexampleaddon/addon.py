import logging

from cliff.command import Command


class Addon(Command):
    "An addon command that prints a message."

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        self.log.info('addon sending greeting')
        self.log.debug('addon debugging')
        self.app.stdout.write('addon hi!\n')
