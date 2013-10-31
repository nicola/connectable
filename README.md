# connectable

connectable is an open source library writtern in Python that makes sensors, devices and apps connectable and programmable. Deploying it to a computer, mobile, watch, it transform your device into a droid that execute some actions at some given triggers.

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
