edu.mit.media.funf.probe.builtin.MagneticFieldSensorProbe -- 566403
edu.mit.media.funf.probe.builtin.GyroscopeSensorProbe 549537
edu.mit.media.funf.probe.builtin.PressureSensorProbe
edu.mit.media.funf.probe.builtin.ProcessStatisticsProbe
	too much info
edu.mit.media.funf.probe.external.UserStudyNotificationProbe
edu.mit.media.funf.probe.builtin.WifiProbe
edu.mit.media.funf.probe.builtin.SmsProbe
  not useful because it's all hashed (probably by gchat?)
edu.mit.media.funf.probe.builtin.LocationProbe
    ignore
edu.mit.media.funf.probe.builtin.RunningApplicationsProbe
edu.mit.media.funf.probe.builtin.CallLogProbe
	useless



edu.mit.media.funf.probe.builtin.TelephonyProbe
edu.mit.media.funf.probe.builtin.ProximitySensorProbe -- 702


edu.mit.media.funf.probe.builtin.BluetoothProbe -- 164
edu.mit.media.funf.probe.builtin.ScreenProbe -- 56


edu.mit.media.funf.probe.builtin.BatteryProbe

edu.mit.media.funf.probe.builtin.ActivityProbe
   useful -- "how active a person is"

edu.mit.media.funf.probe.builtin.SimpleLocationProbe

edu.mit.media.funf.probe.builtin.AccelerometerSensorProbe


1a) outline:
	activity negatively correlated with SMS
		i don't walk and text

	proximity positively correlated with screen on
		i pick up the phone when i turn it on

	|acceleration| positively correlated with phone calls
		phone moves most when talking

1b) correlation coefficients

2a) crunch battery #s

2b) find max \delta battery, min \delta battery

2c) compare to posted HTC specs

3) graph

	3a easy

	3b let's look at SMS freq/activity
