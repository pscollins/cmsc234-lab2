import unittest

from model import *

class TestModel(unittest.TestCase):

    def make_query(self, like_str):
        return session.query(Data.value).filter(
            Data.probe.like("%{}".format(like_str))).first()[0]

    def extract_properties(self, props, ob1):
        return {prop: getattr(ob1, prop) for prop in props}

    def expect_props(self, obj, props):
        self.assertTrue(all(getattr(obj, k) == v for k, v in props.items()))

    def test_activity(self):
        v = self.make_query('ActivityProbe')
        expected = ActivtyLevel(level='high', ts=1428974015.959)
        actual = ActivtyLevel.parse(v)

        extr = lambda o: self.extract_properties(['level', 'ts'], o)

        self.assertEqual(extr(expected), extr(actual))

    def test_proximity(self):
        v = self.make_query('ProximitySensorProbe')
        expected = {
            'is_close': False,
            'ts': 1429017898.312135
        }
        self.expect_props(Proximity.parse(v), expected)

    def test_acceleration(self):
        actual = Acceleration.parse(self.make_query("AccelerometerSensorProbe"))
        expected = {
            'x': 1.26,
            'y': 4.73,
            'z': 10.889999
        }

        self.expect_props(actual, expected)

    def test_screen(self):
        self.expect_props(ScreenOn.parse(self.make_query("ScreenProbe")), {
            'is_on': True})

    def test_battery(self):
        self.expect_props(Battery.parse(self.make_query('BatteryProbe')), {
            'plugged_in': False,
            'temperature': 331,
            'level': 97,
        })


if __name__ == '__main__':
    unittest.main()
