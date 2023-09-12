Entity: ImplementModel 
================
 
Global description: **This entity contains a harmonised description of a generic implement (inspired by the ISOBUS standard).** 

## List of properties 

### Static

- `id`: Unique identifier of the entity 
- `type`: NGSI Entity Type. It has to be ImplementModel 
- `name`: The name of this item.
- `brandName`: The brand of the implement
- `modelName`: The name of the model
- `implementType`: Implement type based on description in ISOBUS 11783 (enum: Non-specific System, Secondary Tillage, Planters/Seeders, Fertilizers, Sprayers, Harvesters, Root Harvesters, Forage, Irrigation, Transport/Trailer, Farm Yard Operations, Powered Auxiliary Devices, Special Crops, Earth Work, Skidder, Sensor Systems, Timber Harvesters, Forwarders, Timber Loaders, Timber Processing Machines, Mulchers, Slurry/Manure Applicators, Feeders/Mixers, Weeders) 
- `PTO`: If the implement requires PTO
- `auxValve`: The amount of auxiliary valves required
- `valve`: (**TBD**)
- `actuationType`: (**TBD**)
- `actuationNumber`: (**TBD**. e.g. valve, heat, elec. power)
- `height`: The height of the implement model, in meters
- `width`: The width of the implement model, in meters
