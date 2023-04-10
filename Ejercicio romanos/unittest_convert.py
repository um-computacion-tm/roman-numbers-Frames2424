#Importo unittest 
import unittest

#Importo convert del archivo convert_roman_to_decimal.py 

from convert_roman_to_decimal import Convert

#creo la clase de test decimal_to_roman
class TestDecimalToRoman(unittest.TestCase): 
    def testDecimalToRoman_I(self):
        converter = Convert()
        result = converter.decimalToRoman(1)
        self.assertEqual(result, 'I')
    def testDecimalToRoman_II(self):
        converter = Convert()
        result = converter.decimalToRoman(4)
        self.assertEqual(result, 'IV')
    def testDecimalToRoman_III(self):
        converter = Convert()
        result = converter.decimalToRoman(5)
        self.assertEqual(result, 'V')
    def testDecimalToRoman_IV(self):
        converter = Convert()
        result = converter.decimalToRoman(9)
        self.assertEqual(result, 'IX')
    def testDecimalToRoman_V(self):
        converter = Convert()
        result = converter.decimalToRoman(10)
        self.assertEqual(result, 'X')
    def testDecimalToRoman_VI(self):
        converter = Convert()
        result = converter.decimalToRoman(40)
        self.assertEqual(result, 'XL')
    def testDecimalToRoman_VII(self):
        converter = Convert()
        result = converter.decimalToRoman(50)
        self.assertEqual(result, 'L')
    def testDecimalToRoman_VIII(self):
        converter = Convert()
        result = converter.decimalToRoman(90)
        self.assertEqual(result, 'XC')
    def testDecimalToRoman_IX(self):
        converter = Convert()
        result = converter.decimalToRoman(100)
        self.assertEqual(result, 'C')
    def testDecimalToRoman_X(self):
        converter = Convert()
        result = converter.decimalToRoman(99)
        self.assertEqual(result, 'XCIX')
    def testDecimalToRoman_XI(self):
        converter = Convert()
        result = converter.decimalToRoman(1001)
        self.assertEqual(result, 'MI')
    def testDecimalToRoman_XII(self):
        converter = Convert()
        result = converter.decimalToRoman(6)
        self.assertEqual(result, 'VI')
    def testDecimalToRoman_XIII(self):
        converter = Convert()
        result = converter.decimalToRoman(7)
        self.assertEqual(result, 'VII')
    def testDecimalToRoman_XIV(self):
        converter = Convert()
        result = converter.decimalToRoman(8)
        self.assertEqual(result, 'VIII')
    def testDecimalToRoman_XV(self):
        converter = Convert()
        result = converter.decimalToRoman(1109)
        self.assertEqual(result, 'MCIX')
    def testDecimalToRoman_XVI(self):
        converter = Convert()
        result = converter.decimalToRoman(60)
        self.assertEqual(result, 'LX')
    def testDecimalToRoman_XVII(self):
        converter = Convert()
        result = converter.decimalToRoman(70)
        self.assertEqual(result, 'LXX')
    def testDecimalToRoman_XVIII(self):
        converter = Convert()
        result = converter.decimalToRoman(80)
        self.assertEqual(result, 'LXXX')
    def testDecimalToRoman_XIX(self):
        converter = Convert()
        result = converter.decimalToRoman(20)
        self.assertEqual(result, 'XX')
    def testDecimalToRoman_XX(self):
        converter = Convert()
        result = converter.decimalToRoman(30)
        self.assertEqual(result, 'XXX')
    def testDecimalToRoman_XXI(self):
        converter = Convert()
        result = converter.decimalToRoman(35)
        self.assertEqual(result, 'XXXV')
    def testDecimalToRoman_XXII(self):
        converter = Convert()
        result = converter.decimalToRoman(76)
        self.assertEqual(result, 'LXXVI')
    def testDecimalToRoman_XXIII(self):
        converter = Convert()
        result = converter.decimalToRoman(89)
        self.assertEqual(result, 'LXXXIX')
    def testDecimalToRoman_XXIV(self):
        converter = Convert()
        result = converter.decimalToRoman(80)
        self.assertEqual(result, 'LXXX')
    def testDecimalToRoman_XXIX(self):
        converter = Convert()
        result = converter.decimalToRoman(999)
        self.assertEqual(result, 'CMXCIX')
    def testDecimalToRoman_XXX(self):
        converter = Convert()
        result = converter.decimalToRoman(305)
        self.assertEqual(result, 'CCCV')
    def testDecimalToRoman_XXXIII(self):
        converter = Convert()
        result = converter.decimalToRoman(996)
        self.assertEqual(result, 'CMXCVI')
    def testDecimalToRoman_XXXIV(self):
        converter = Convert()
        result = converter.decimalToRoman(886)
        self.assertEqual(result, 'DCCCLXXXVI')
    def testDecimalToRoman_XXXVII(self):
        converter = Convert()
        result = converter.decimalToRoman(85)
        self.assertEqual(result, 'LXXXV')

    
class TestRomanToDecimal(unittest.TestCase):

    def testRomanToDecimal_I(self):
        converter = Convert()
        result = converter.romanToDecimal('I')
        self.assertEqual(result, 1)
    def testRomanToDecimal_II(self):
        converter = Convert()
        result = converter.romanToDecimal('II')
        self.assertEqual(result, 2)
    def testRomanToDecimal_III(self):
        converter = Convert()
        result = converter.romanToDecimal('IV')
        self.assertEqual(result, 4)
    def testRomanToDecimal_IV(self):
        converter = Convert()
        result = converter.romanToDecimal('V')
        self.assertEqual(result, 5)
    def testRomanToDecimal_V(self):
        converter = Convert()
        result = converter.romanToDecimal('VI')
        self.assertEqual(result, 6)
    def testRomanToDecimal_XV(self):
        converter = Convert()
        result = converter.romanToDecimal('CCXLV')
        self.assertEqual(result, 245)
    def testRomanToDecimal_XVI(self):
        converter = Convert()
        result = converter.romanToDecimal('CCCXXXIII')
        self.assertEqual(result, 333)
    def testRomanToDecimal_XVII(self):
        converter = Convert()
        result = converter.romanToDecimal('CDLIX')
        self.assertEqual(result, 459)
    def testRomanToDecimal_XVIII(self):
        converter = Convert()
        result = converter.romanToDecimal('CMXCIX')
        self.assertEqual(result, 999)
    def testRomanToDecimal_VI(self):
        converter = Convert()
        result = converter.romanToDecimal('IX')
        self.assertEqual(result, 9)
    def testRomanToDecimal_VII(self):
        converter = Convert()
        result = converter.romanToDecimal('X')
        self.assertEqual(result, 10)
    def testRomanToDecimal_VIII(self):
        converter = Convert()
        result = converter.romanToDecimal('XXXVI')
        self.assertEqual(result, 36)
    def testRomanToDecimal_IX(self):
        converter = Convert()
        result = converter.romanToDecimal('XLI')
        self.assertEqual(result, 41)
    def testRomanToDecimal_X(self):
        converter = Convert()
        result = converter.romanToDecimal('XLVII')
        self.assertEqual(result, 47)
    def testRomanToDecimal_XI(self):
        converter = Convert()
        result = converter.romanToDecimal('XCVIII')
        self.assertEqual(result, 98)
    def testRomanToDecimal_XIX(self):
        converter = Convert()
        result = converter.romanToDecimal('DCLXVI')
        self.assertEqual(result, 666)
    def testRomanToDecimal_XII(self):
        converter = Convert()
        result = converter.romanToDecimal('LVI')
        self.assertEqual(result, 56)
    def testRomanToDecimal_XIII(self):
        converter = Convert()
        result = converter.romanToDecimal('LXXVII')
        self.assertEqual(result, 77)
    def testRomanToDecimal_XIV(self):
        converter = Convert()
        result = converter.romanToDecimal('CXXIII')
        self.assertEqual(result, 123)




    
    
    



if __name__ == '__main__':
    unittest.main()
