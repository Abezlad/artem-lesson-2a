#1
value = 99

new_value = value / 2 if value < 100 else value * 2
print( new_value )

# 2
value = 99
new_value = 1 if value > 100 else 0
print( new_value )

# 3
#
value = 99
new_value = True if value > 100 else False

print( new_value )
#
#4

value = "helo"

new_value = value*2 if len(value) < 5 else value
print( new_value )
#
#5
value = "helo"
new_value = value + value[::-1] if len(value) < 5 else value # 5


print( new_value )