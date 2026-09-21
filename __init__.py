# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later
"""QGIS loader for Find Duplicate."""


def classFactory(iface):
    from .fd_plugin import FindDuplicatePlugin
    return FindDuplicatePlugin(iface)
