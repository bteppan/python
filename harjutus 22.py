import datetime

kp = datetime.datetime.now()
print(kp)

print(kp.strftime("%d.%m %Y, %H:%M:%S"))
sp = datetime.datetime(2009,11,15)
vanus_paevades = kp - sp
print(f"vanus päevades: {vanus_paevades}")
vanus_aastates = vanus_paevades // 365
print(f"Vanus aastates: {vanus_aastates}")