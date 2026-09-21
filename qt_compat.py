# SPDX-License-Identifier: GPL-3.0-or-later
"""Field type enums selected for the active Qt binding."""
from qgis.PyQt.QtCore import QT_VERSION_STR

if int(QT_VERSION_STR.split('.')[0]) >= 6:
    from qgis.PyQt.QtCore import QMetaType
    FIELD_STRING = QMetaType.Type.QString
    FIELD_INT = QMetaType.Type.Int
else:
    from qgis.PyQt.QtCore import QVariant
    FIELD_STRING = QVariant.String
    FIELD_INT = QVariant.Int
