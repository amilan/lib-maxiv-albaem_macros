#!/usr/bin/env python

###############################################################################
#     albaem_macros
#
#     Copyright (C) 2017  MAX IV Laboratory, Lund Sweden.
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see [http://www.gnu.org/licenses/].
###############################################################################

"""Main module."""

import socket

from sardana.macroserver.macro import macro, Type, Macro


class EMSocket(socket.socket):
    FAMILY = socket.AF_INET
    S_TYPE = socket.SOCK_STREAM
    args = [FAMILY, S_TYPE]

    def __init__(self, em_host, em_port=5025, *args, **kwargs):
        socket.socket.__init__(self, *args, **kwargs)
        self.em_host = em_host
        self.em_port = em_port

    def __enter__(self):
        self.connect((self.em_host, self.em_port))
        self.settimeout(0.1)
        return self

    def __exit__(self, *args, **kwargs):
        # print args
        # print kwargs
        self.close()

# @macro([['albaem_host', str,   None, 'EM host name'],
#         ['mode',  int,   None, 'Mode to be applied']])
# def set_albaem_mode(self, albaem_host, mode):


class set_albaem_mode(Macro):
    """Set AlbaEM multiplexor mode."""

    param_def = [
        ['albaem_host', Type.String,   None, 'EM host name'],
        ['mode',  Type.Integer,   None, 'Mode to be applied']
    ]

    def run(self, albaem_host, mode):
        """Set AlbaEM multiplexor mode."""
        EM = albaem_host
        MODE = mode

        with EMSocket(EM) as ems:
            ems.send("IOPO05:CONF 0;IOPO06:CONF 0;IOPO07:CONF 0\n")
            a0 = MODE & 1 > 0
            a1 = MODE & 2 > 0
            a2 = MODE & 4 > 0
            msg = "A0: {0}, A1: {1}, A2: {2}".format(a0, a1, a2)
            self.output(msg)
            # print a0, a1, a2
            cmd = "IOPO05:VALU %d;IOPO06:VALU %d;IOPO07:VALU %d\n" % (a0, a1, a2)
            ems.send(cmd)
