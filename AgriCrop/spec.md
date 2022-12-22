Entity: AgriCrop
================

Global description: **This entity contains a harmonised description of a generic crop. This entity is primarily associated with the agricultural vertical and related IoT applications.**  


version: 0.0.4  


## List of properties  


[*] If there is not a type in an attribute is because it could have several types or different formats/patterns

- `agroVocConcept[string]`: The link with the defined concept into the AgroVoc vocabulary  . Model: [http://schema.org/URL](http://schema.org/URL)
- `alternateName[string]`: An alternative name for this item  
- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity.  
- `dateCreated[string]`: Entity creation timestamp. This will usually be allocated by the storage platform.  
- `dateModified[string]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  
- `description[string]`: A description of this item  
- `harvestingInterval[array]`: A list of the recommended harvesting interval date(s) for this crop. Specified using ISO8601 repeating date intervals:

 **interval, description**

 Where **interval** is in the form of **start date/end date**

 --MM-DD/--MM-DD

 Meaning repeat each year from this start date to this end date.  . Model: [http://schema.org/URL](http://schema.org/URL)
- `hasAgriFertiliser[array]`: Reference to the recommended types of fertiliser suitable for growing this crop.  . Model: [http://schema.org/URL](http://schema.org/URL)
- `hasAgriPest[array]`: Reference to the pests known to attack this crop  . Model: [https://schema.org/URL](https://schema.org/URL)
- `hasAgriSoil[array]`: Reference to the recommended types of soil suitable for growing this crop.  . Model: [http://schema.org/URL](http://schema.org/URL)
- `id[*]`: Unique identifier of the entity  
- `name[string]`: The name of this item.  
- `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `plantingFrom[array]`: A list of the recommended planting interval date(s) for this crop. Specified using ISO8601 repeating date intervals:

**interval, description**

Where **interval** is in the form of **start date/end date**

--MM-DD/--MM-DD

Meaning repeat each year from this start date to this end date.  . Model: [http://schema.org/URL](http://schema.org/URL)
- `relatedSource[array]`: List of IDs the current entity may have in external applications  
- `seeAlso[*]`: list of uri pointing to additional resources about the item  
- `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `type[string]`: NGSI Entity Type. it has to be AgriCrop  


Required properties  
- `id`  
- `name`  
- `type`  


This entity is primarily associated with the agricultural vertical and related IoT applications.  
