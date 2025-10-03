# 🔧 2. Function Arguments & Return Values
# Q:
# Create a function area_calc(length, width=1) that:

# Calculates area as length * width

# If no width is given, assume it's a square

# Return the area

# 📥 Test Cases:

# area_calc(4) → 4
# area_calc(5, 3) → 15

def area_calc(len , width=1):
      return len*width
print(area_calc(4))
print(area_calc(5,3))