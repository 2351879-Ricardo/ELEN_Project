import unittest
import CODE.calculation as energyCalc

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

# Added to thes version 0.2
# Unlike the first set of tests - thes tests are dependant on the unitconverter moudle
class testEnergyCalc_2(unittest.TestCase):
    def test_fuelEnergy_petrol_1(self):
        self.assertAlmostEqual(energyCalc.fuelEnergy("petrol", 32.1), 304.95)
    def test_fuelEnergy_diesel_1(self):
        self.assertAlmostEqual(energyCalc.fuelEnergy("diesel", 32.1), 344.112)

    def test_energyUsed_1(self):
        self.assertAlmostEqual(energyCalc.energyUsed(1012.6, 1000.1, 6.2, "petrol"), 7.3625)
    def test_energyUsed_2(self):
        self.assertAlmostEqual(energyCalc.energyUsed(3421, 3386.2, 7.82, "diesel"), 29.1729792)
if __name__ == '__main__':
    unittest.main()