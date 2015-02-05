__author__ = 'Lada'

oneto9="onetwothreefourfivesixseveneightnine"
tento19="teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen"
twentyto99="twentythirtyfortyfiftysixtyseventyeightyninety"

h="hundred"

s1=len(oneto9)+len(tento19)+10*len(twentyto99)+9*len(oneto9)
s2=9*len(h)+len(oneto9)

s3=9*99*(s2+len("and"))
s4=len("thousand")

s0=s1+s2+s3+s4

print("The solution is " +str(s0))

