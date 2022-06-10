#!/usr/bin/env python3

# Power.log by GROOP - 2022
# Programed by J Jandrell 

import unittest
import unitConverter

class testEnergy2Litres(unittest.TestCase):
	# A trivial test
	def test_lDesel2kwh_1(self):
		self.assertEqual(10.72,unitConverter.lDesel2kwh(1))
	
	# A random case 
	def test_lDesel2kwh_2(self):
		self.assertAlmostEqual(57.888, unitConverter.lDesel2kwh(5.4))
	
	# A trivial case
	def test_kwh2lDesel_1(self):
		self.assertEqual(1,unitConverter.kwh2lDesel(10.72))
	
	# A random case
	def test_kwh2lDesel_2(self):
		self.assertAlmostEqual(4.38432836, unitConverter.kwh2lDesel(47))

	def test_lPetrol2kwh_1(self):
		self.assertAlmostEqual(9.5,unitConverter.lPetrol2kwh(1))
	def test_lPetrol2kwh_2(self):
		self.assertAlmostEqual(125.4,unitConverter.lPetrol2kwh(13.2))
	
	def test_kwh2lPetrol_1(self):
		self.assertAlmostEqual(1, unitConverter.kwh2lPetrol(9.5))
	def test_kwh2lPetrol_2(self):
		self.assertAlmostEqual(5.36842105,unitConverter.kwh2lPetrol(51))

	def test_kwh2MJ_1(self):
		self.assertAlmostEqual(unitConverter.kwh2MJ(7.4),26.64)
	def test_MJ2kwh(self):
		self.assertAlmostEqual(unitConverter.MJ2kwh(3.2),0.8888889)

class testTimeConversions(unittest.TestCase):
	def test_sec2min_1(self):
		self.assertAlmostEqual(unitConverter.sec2min(93), 1.55)
	def test_min2sec_1(self):
		self.assertAlmostEqual(unitConverter.min2sec(0.25),15)
	
	def test_min2hour_1(self):
		self.assertAlmostEqual(unitConverter.min2hour(77), 1.28333333)
	def test_hour2min_1(self):
		self.assertAlmostEqual(unitConverter.hour2min(23.51),1410.6)
	
	def test_hour2day_1(self):
		self.assertAlmostEqual(unitConverter.hour2day(52), 2.1666667)
	def test_day2hour_1(self):
		self.assertAlmostEqual(unitConverter.day2hour(17.2),412.8)
	
	def test_time2day(self):
		hours = 11
		minutes = 34
		seconds = 43
		self.assertAlmostEqual(unitConverter.time2day(hours,minutes,seconds),0.48244213)
	def test_day2time_1(self):
		hours, minutes, seconds = unitConverter.day2time(4.2)
		self.assertAlmostEqual(hours, 100)
		self.assertAlmostEqual(minutes, 48)
		self.assertAlmostEqual(seconds, 0)
	def test_day2time_2(self):
		hours, minutes, seconds = unitConverter.day2time(5.61)
		self.assertAlmostEqual(hours, 134)
		self.assertAlmostEqual(minutes, 38)
		self.assertAlmostEqual(seconds, 24)

class test_siPrefix(unittest.TestCase):
	def test_siPrefix_1(self):
		self.assertAlmostEqual(unitConverter.siPrefix(3.1, 'k'), 3100)
	def test_siPrefix_2(self):
		self.assertAlmostEqual(unitConverter.siPrefix(-1700000, ' ', 'M'), -1.7)
	def test_siPrefix_3(self):
		self.assertAlmostEqual(unitConverter.siPrefix(11, 'n', 'mu'), 0.011)
	def test_siPrefix_4(self):
		self.assertAlmostEqual(unitConverter.siPrefix(0.98, 'Y', 'Z'), 980)
	def test_siPrefix_5(self):
		self.assertAlmostEqual(unitConverter.siPrefix(1.2, 'd', 'c', 2), 120)

if __name__ == '__main__':
	unittest.main()

