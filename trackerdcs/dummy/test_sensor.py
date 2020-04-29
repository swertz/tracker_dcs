import unittest
from .sensor import Sensor


class TestSensor(unittest.TestCase):


    def test_1(self):
        sensor = Sensor('sensor_1')
        self.assertDictEqual(sensor.status(0),
                             {'meas1': 0.,
                              'meas2': 0.})
