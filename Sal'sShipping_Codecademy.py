import random

# Random_weight_function
WOP = random.randint(1, 100)
print('Package Weight:', WOP, 'lb')

# Ground Shipping Variables

# Ground Shipping Standard Parameters
GST = 'Ground Shipping Total:'
GSFC = 20.00

if WOP <= 2:
    GSTC = WOP * 1.50 + GSFC
elif WOP <= 6:
    GSTC = WOP * 3.00 + GSFC
elif WOP <= 10:
    GSTC = WOP * 4.00 + GSFC
else:
    GSTC = WOP * 4.75 + GSFC

print(GST, '$', GSTC)

# Ground Shipping Premium Parameters
GPT = 'Ground Premium Total:'
GPFC = 125.00
print(GPT, '$', GPFC)

# Drone Shipping Parameters
DSFC = 0.00
DST = 'Drone Shipping Total:'

if WOP <= 2:
    DSFC += WOP * 4.50
elif WOP <= 6:
    DSFC += WOP * 9.00
elif WOP <= 10:
    DSFC += WOP * 12.00
else:
    DSFC += WOP * 14.25

print(DST, '$', DSFC)

# Compare shipping costs
if (GSTC < DSFC) and (GSTC < GPFC):
    print('Ground Shipping is Cheapest!')
elif (DSFC < GSTC) and (DSFC < GPFC):
    print('Drone Shipping is the Cheapest!')
elif (GPFC < GSTC) and (GPFC < DSFC):
    print('Ground Premium is the Cheapest!')
else:
    print('Ground Premium is the Cheapest!')
