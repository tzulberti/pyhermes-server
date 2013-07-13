# -*- coding: utf-8 -*-

class Service(object):
    '''Represents something that will be executed on the client to
    validate if everything is ok.

    For example, there are services that will check:

    - Disk usage
    - CPU usage
    - Is a process is running
    - RAM used


    :param name: the service name.
    :param description: a description of what the service is doing.
    :param command: the :class:`pyhermes_server.configuration.command.Command`
                    that the service will execute.
    :param command_args: the list of arguments that will be used on the
                         command.
    '''
