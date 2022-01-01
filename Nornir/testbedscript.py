#Python script to generate a Genie Testbed file
#Substitute username / password for your own
#Modify the IP addresses and loop range as required

print("---")
print("testbed:")
print("\n  credentials:")
print("    default:")
print("      username: \"geordie\"")
print("      password: \"teabag\"")

print("\ndevices:")

for i in range(1, 15):
  print(" R" + str(i) + ":")
  print("   alias: R" + str(i))
  print("   ios")
  print("   type: ios")
  print("   connections:")

  print("\n      defaults:")
  print("        class:unicon.Unicon")
  print("       console:")
  print("         protocol: ssh")
  print("         IP: 192.167.1." + str(i))
  print("\n     custom:")
  print("       abstraction:")
  print("           order: [os, type]\n")

