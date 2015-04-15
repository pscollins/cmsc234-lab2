from model import *

FMT = "edu.mit.media.funf.probe.builtin.{}"
SENSORS = {
    'ActivityProbe': ActivtyLevel,
    'ProximitySensorProbe': Proximity,
    'AccelerometerSensorProbe': Acceleration,
    'ScreenProbe': ScreenOn,
    'BatteryProbe': Battery
}

def main():
    i = 0
    for row in session.query(Data.probe, Data.value).filter(Data.probe.in_([
            FMT.format(sen) for sen in SENSORS.keys()])).all():
        if not i % 10000:
            print("Parsing row ", i)

        probe = row[0].split('.')[-1]
        to_add = SENSORS[probe].parse(row[1])
        session.add(to_add)
        i += 1
    session.commit()

if __name__ == '__main__':
    main()
