Entity: AgriSoil
================

Global description: **This entity contains a harmonised description of a generic soil. This entity is primarily associated with the agricultural vertical and related IoT applications.**  

version: 0.0.2  


## List of properties  


[*] If there is not a type in an attribute is because it could have several types or different formats/patterns

- `agroVocConcept[string]`: Reference to the agrovoc term associated with this item  . Model: [http://schema.org/URL](http://schema.org/URL)
- `alternateName[string]`: An alternative name for this item  
- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity.  
- `dateCreated[string]`: Entity creation timestamp. This will usually be allocated by the storage platform.  
- `dateModified[string]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  
- `description[string]`: A description of this item  
- `hasAgriProductType[array]`: Reference to the recommended types of product (such as fertiliser) that can be used to condition this soil type.  
- `id[*]`: Unique identifier of the entity  
- `name[string]`: The name of this item.  
- `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `relatedSource[array]`: List of IDs the current entity may have in external applications  
- `seeAlso[*]`: list of uri pointing to additional resources about the item  
- `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `type[string]`: NGSI Entity Type: It has to be AgriSoil  



Required properties  
- `id`  
- `name`  
- `type`  


This entity is primarily associated with the agricultural vertical and related IoT applications.  
