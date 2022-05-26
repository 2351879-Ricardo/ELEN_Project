# Power.log by GROOP - 2022
# Programed by Joshua Jnadrell 

import math

# ==================================================
# -------- Litres to energy conversions ------------
# ==================================================
# constant coefficents
DESEL_KWH_PER_LITRE = 10.72
PETROL_KWH_PER_LITRE = 9.500

#Desel
def lDesel2kwh(litres):
	return DESEL_KWH_PER_LITRE * litres

def kwh2lDesel(kwh):
	return kwh / DESEL_KWH_PER_LITRE

#Petrol
def lPetrol2kwh(litres):
	return litres * PETROL_KWH_PER_LITRE

def kwh2lPetrol(kwh):
	return kwh / PETROL_KWH_PER_LITRE
# ==================================================
# ----------- Other energy conversions -------------
# ==================================================
def kwh2MJ(kwh):
	return kwh * 3.6
def MJ2kwh(megaJoules):
	return megaJoules / 3.6
# ==================================================
# --------------- Time conversions -----------------
# ==================================================
def sec2min(seconds):
	return seconds / 60
def min2sec(minutes):
	return minutes * 60

def min2hour(minutes):
	return minutes / 60
def hour2min(hours):
	return hours * 60

def sec2hour(seconds):
	return seconds / 3600
def hour2sec(hours):
	return hours * 3600
	
def hour2day(hours):
	return hours / 24
def day2hour(days):
	return days * 24
	
def time2day(hours, minutes, seconds):
	return hour2day(hours + min2hour(minutes) +sec2hour(seconds))
def day2time(days):
	_hours = day2hour(days)
	_minutes = hour2min(_hours % 1)
	_seconds = min2sec(_minutes % 1) 
	return math.floor(_hours), math.floor(_minutes), math.floor(_seconds)

# ==================================================
# --------------SI perfex conversions --------------
# ==================================================
def siPrefix(value, prefixFrom, prefixTo = " ", degree = 1):
	prefixes = {
		'Y':10**24,
		'Z':10**21,
		'E':10**18,
		'P':10**15,
		'T':10**12,
		'G':10**9,
		'M':10**6,
		'k':10**3,
		' ':1,
		'd':10**(-1),
		'c':10**(-2),
		'm':10**(-3),
		'mu':10**(-6),
		'n':10**(-9),
		'p':10**(-12),
		'f':10**(-15),
		'a':10**(-18),
		'z':10**(-21),
		'y':10**(-24)
	}
	return value * ((prefixes[prefixFrom]/prefixes[prefixTo])**degree)
	
	
