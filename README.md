# connectable

Connectable defines a standard to connect triggers and actions of hardware and software, making everything around you connectable and programmable.

## Proof of concept
Here are two main examples when connectable is applied to a smart house / house automation system through a Raspberry PI and to a life-logging watch with body sensors.

>  When (I am entering the house AND it is 5pm AND I am with Kapil) then (play Snoop Dogg)

 
>  When (I am running AND heart beat is > 80bps) then (send me a message to have a break)
 

## Structure

A connectable instance will have `Device`s connected, and these will have two attributes: `trigger`s and `action`s.

### Device
connectable recognises as `Device` anything that can be connected to it through cable, bluetooth, wifi (`transport`) and as mentioned earlier, it can be user as trigger or as action.

#### Trigger
When a trigger occurs, an action is executed.

```
// Blood pressure sensor example with 2 triggers
{
  family: "sensors/bloodpressure",
  name: "Blood pressure sensor",
  mac: "20:c9:d0:7d:05:11",
  triggers: {
    "bloodpressure-in-range": {
      name:"Bloodpress is less than",
      "fields": {
        "min-value": Number,
        "max-value": Number
      }
    },
    "bloodpressure-increases": {}
    [...]
  },
  actions: []
}
```

#### Action
Each action will be specified in a JSON file
Action 

```
// Music player with one trigger
{
  family: "device/stereo",
  name: "Music player",
  mac: "20:c9:d0:7d:05:11",
  triggers: {},
  actions: {
    "play_song": {
      "song-id": String,
      "volume": Number
    },
    "volume": {
      "value": Number
    }
  }
}
```

### Scripting language
A jQuery inspired scripting language (temporarely called RennieScript) will be used to generate script.json files:

```
 script = connectable.Script()
 script
     .when(IDCardScanner,"scanned_card", {people: ["Kapil"]})
     .when(TimeSensor,"current_time", {hour: "12pm"})
     .then(HiFi, "play", "Snoop Dogg")
     .then(LightDimmer, "dim", "30%")
```

And for creating devices

```
 device = connectable.Device("Camera")
 device
     .trigger("shoot_pressed", {pressed: Boolean}, listen_shoot, execute_at_shooting)
     .trigger("face_recognised", {people: [String]}, listen_camera_for_recognition, execute_when_person_is_recognised)
     .action("take_picture", "", execute_after_picture_taken)
```

For reading sensors

```
 heartbeat = connectable.Device("health/heartbeat", "Heartbeat_sensor")
 heartbeat.read("get_heartbeat")
 // {now: "27"}
 hifi.read("Stereo", "current_volume")
 // {volume: "80%"}
```

Performing actions

```
 hifi.do("volume", "90%")
```