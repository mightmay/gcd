import pytest
def test_gcd_positive_values():
 """Should return positive gcd."""
 assert 5 == gcd(30, 35)
 assert 4 == gcd(48, 20)
def test_gcd_no_common_factors():
 """gcd of relatively primes values is 1."""
 assert 1 == gcd(30, 49)
 assert 1 == gcd(27, 29)
 assert 1 == gcd(44, 1)
