Entity: AgriRobot  
================
  
Global description: **This entity contains a harmonised description of a generic agri robot model.**  

## List of properties  

### Static

- `id`: Unique identifier of the entity  
- `type`: NGSI Entity Type. It has to be AgriRobot  
- `name`: The name of this item.  
- `hasFarm`: Id of the farm in which the robot is operating
- `refRobotModel`: The id of the reference model
- `category`: (enum: **TBD**)
- `serviceProvided`: List of services provided by the robot (**TBD**)
- `hasImplement`: List of the mounted implement ids 
- `hasDevice`: List of the mounted device ids
- `cmdList`: List of the commands that rebot is capable to execute

### Dynamic

- `status`:   List of service statuses, one for each provided service
- `hitch`:    (**TBD**), in ??
- `location`: Location of the robot, GEOJSON point
- `speed`:    (**TBD**), in ??
- `bearing`:  (**TBD**), in ??
- `heading`:  (**TBD**), in ??
- `cmd`: The last received command; this is a JSON Object (e.g., `{ "startMission": "mission-identifier" }`)
