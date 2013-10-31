# Droidable

Droinable is an open source library written in Python that connects devices, sensors and apps in unique place (computer, mobile phone, watch), transforming the device into a droid that executes some actions at given triggers.

Droidable is an open source library writtern in Python that makes connectable and programmable sensors, devices and apps. Deploying it to a computer, mobile, watch, it transform your device into a droid that execute some actions at some given triggers.

## Proof of concept
Here are two main examples when Droidable is applied to a smart house / house automation system through a Raspberry PI and to a life-logging watch with body sensors.

>  When (I am entering the house AND it is 5pm AND I am with Kapil) than (play Snoop Dogg)

 
>  When (I am running AND heart beat is > 80bps) than (send me a message to have a break)
 

## Structure

A droidable instance will have `Device`s connected, and these will have two attributes: `trigger`s and `action`s.

### Device
Droidable recognises as `Device` anything that can be connected to it through cable, bluetooth, wifi (`transport`) and as mentioned earlier, it can be user as trigger or as action.

#### Trigger
When a trigger occurs, an action is executed.

```
// Blood pressure sensor example with 2 triggers
{
  device: "sensors/bloodpressure",
  name: "Blood pressure sensor",
  mac: "20:c9:d0:7d:05:11",
  triggers: [{
    "bloodpressure-in-range": {
      name:"Bloodpress is less than",
      "fields": {
        "min-value": Number,
        "max-value": Number
      }
    },
    "bloodpressure-increases": {}
    [...]
  }],
  actions: []
}
```

#### Action
Each action will be specified in a JSON file
Action 

```
// Music player with one trigger
{
  device: "device/stereo",
  name: "Music player",
  mac: "20:c9:d0:7d:05:11",
  triggers: [],
  actions: [{
    "play_song": {
      "song-id": String,
      "volume": Number
    },
    "volume": {
      "value": Number
    }
  }]
}
```
