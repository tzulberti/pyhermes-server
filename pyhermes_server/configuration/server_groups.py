# -*- coding: utf-8 -*-


class ServerGroup(object):
    ''' Represents the list of servers which will have the same
    services.

    One :class:`pyhermes_server.configuration.server.Server` could
    belong to one or more groups.

    :param name: the group name.
    :param servers: a list that could have more or one
                    :class:`pyhermes_server.configuration.server.Server`
    :param services: a list of one or more
                     :class:`pyhermes_server.configuration.service.Service`
                     that each of this servers will execute
    '''
