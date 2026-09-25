# Find Duplicate

Find Duplicate is a QGIS plugin for identifying duplicate and unique values in
one selected attribute field. It produces a documented output Shapefile for
data validation and quality-control workflows.

## Main workflow

1. Load a point, line, or polygon vector layer in QGIS, or browse to a vector
   dataset from the plugin.
2. Select the field to check for duplicates.
3. Optionally select other fields to retain in the output.
4. Choose an output Shapefile and run the analysis.

The output keeps the duplicate-check field first, followed by the optional
selected fields. It then adds:

- `NOTES`: `DUPLICATE IDENTIFIED` or `UNIQUE IDENTIFIED`;
- `FREQUENCY`: the number of features containing the same key value;
- `LOCATIONS`: centroid coordinates for every matching feature; and
- `DETAIL`: a readable explanation of the result.

Comparison preserves the stored value type, letter case, and spaces. The
source geometry and coordinate reference system are retained. Coordinates in
`LOCATIONS` use the source layer's CRS; a projected CRS is recommended when
the locations must be interpreted as metric coordinates.

## Shapefile field names

DBF field names are limited to ten characters. Find Duplicate sanitizes and
shortens retained field names, then adds a numeric suffix when two shortened
names would collide. The usual analysis names remain `NOTES`, `FREQUENCY`,
`LOCATIONS`, and `DETAIL`; they are also renamed safely if an input field uses
the same name.

## Safe output handling

The plugin writes the new Shapefile into a temporary directory, reopens it in
QGIS, and verifies its feature count. An existing output is replaced only
after those checks pass. If replacement fails, the plugin attempts to restore
all original Shapefile components.

## Compatibility

- QGIS 3.22 through 3.99
- Windows, Linux, and macOS
- point, line, polygon, and supported multipart vector layers
- ESRI Shapefile output with UTF-8 encoding

## Installation

1. Download the release ZIP from this repository's Releases page.
2. In QGIS, open **Plugins > Manage and Install Plugins**.
3. Select **Install from ZIP**, choose the release ZIP, and install it.
4. Open **Vector > RUANG SPASIAL > Find Duplicate** or use its toolbar icon.

For development, copy the `find_duplicate_fd` directory into the active QGIS
profile's `python/plugins` directory, then restart QGIS.

## Quick test

The `sample_data` directory contains three synthetic polygons in EPSG:32750.
Load `parcels.geojson`, use `parcel_id` as the duplicate-check field, retain
`owner` and `block_name`, and create an output Shapefile. See
`sample_data/README.md` for the expected result.

## Activation

The QGIS edition uses these established License Hub identifiers:

- Product code: `FIDU`
- Fixed code: `SW`
- Trial allowance: two successful analyses
- User guide: <https://aktivasi.ruangspasial.my.id/help/find-duplicate-qgis>

Failed validation or output creation does not consume a trial.

## Support and issues

- User support: <https://aktivasi.ruangspasial.my.id/help/find-duplicate-qgis>
- Bug reports: <https://github.com/purwantodwigeo10/Find-Duplicate/issues>
- Source code: <https://github.com/purwantodwigeo10/Find-Duplicate>

Please include the QGIS version, operating system, input format, geometry type,
steps to reproduce, and exact error message in a bug report. Do not include
activation codes, confidential attributes, or private datasets.

## License

Copyright (C) 2026 Dwi Purwanto / RuangSpasial.

This plugin is free software licensed under the GNU General Public License,
version 3 or any later version. See [LICENSE](LICENSE).
