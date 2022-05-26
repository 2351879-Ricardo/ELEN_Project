import unittest
import calculation.energyCalc

class testEnergyCalc(unittest.TestCase):
    def test_distanceTravelled_1(self):
        self.assertEqual(energyCalc.distanceTravelled(1320, 1255), 65)
    def test_distanceTravelled_2(self):
        self.assertEqual(energyCalc.distanceTravelled(11987, 10241),1746)
    # a trivial case: what if user inputs same reading twice
    def test_distanceTravelled_trivail_1(self):
        self.assertEqual(energyCalc.distanceTravelled(1027,1027),0)
    
    def test_fuelUsed_1(self):
        self.assertAlmostEqual(energyCalc.fuelUsed(142, 8.2), 11.644)
    def test_fuelUsed_2(self):
        self.assertAlmostEqual(energyCalc.fuelUsed(301, 6.3), 18.963)
if __name__ == '__main__':
    unittest.main()