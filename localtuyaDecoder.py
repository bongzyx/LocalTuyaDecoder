# "Beautiful Dim": "07464602000003e8000a00000000464602007803e8000a0000000046460200f003e8000a00000000",
# "Beautiful Bright": "07464602000003e803e800000000464602007803e803e80000000046460200f003e803e800000000",
# "Alert": "08606001016803e800800000000160600100f003e8008000000000",
# "Disco Slow": "08464602000003e803e800000000464602007803e803e80000000046460200f003e803e800000000464602003d03e803e80000000046460200ae03e803e800000000464602011303e803e800000000",
# "Disco Fast": "08636302000003e803e800000000636302007803e803e80000000063630200f003e803e800000000636302003d03e803e80000000063630200ae03e803e800000000636302011303e803e800000000",

# A  B    C  D    E    F    G
# 06 4646 01 0000 03e0 03e8 00000000

# A = No. of entry in the APP aka "scene_num"
# B = "unit_switch_duration" and "unit_gradient_duration"
# C = "unit_change_mode" [“static”,“jump”,“gradient”] (01-02)
# D = four bytes of hue (0-0168)
# E = four bytes of saturation (0-03e8)
# F = four bytes of brightness (0-03e8)
# G = padding (not sure)

# ID SdGd CM hue  sat  bri  padding
# 07 4646 02 0000 03e8 000a 000000
# 00 4646 02 00b4 03e8 000a 000000
# 00 4646 02 0168 03e8 000a 000000
# 00

# ID SdGd CM hue  sat  bri  padding
# 06 6060 01 0168 03e8 03e8 000000
# 00 6060 01 00f0 03e8 03e8 00000000
# 06606001016803e803e80000000060600100f003e803e800000000
bytesSeperator = [2, 2, 2, 2, 4, 4, 4, 6]


def decode(
    strToDecode="07464602000003e8000a00000000464602007803e8000a0000000046460200f003e8000a00000000",
):
    if len(strToDecode) < 26:
        return
    print(f"\n\n\n----------")
    effectSets = []
    numSets = len(strToDecode) // 26
    remainder = len(strToDecode) % 2
    for set in range(1, numSets + 1):
        set = strToDecode[(set - 1) * 26 : set * 26]
        singleSet = []
        for i in bytesSeperator:
            singleSet.append(set[:i])
            set = set[i:]
        effectSets.append(singleSet)

    for set in effectSets:
        sceneNum = int(set[0], 16)
        unitSwitchDuration = int(set[1], 16)
        unitGradientDuration = int(set[2], 16)
        unitChangeMode = int(set[3], 16)
        hue = int(set[4], 16)
        saturation = int(set[5], 16)
        brightness = int(set[6], 16)
        padding = set[7]
        print(f"Scene Number: \t\t{sceneNum}")
        print(f"Unit Switch Duration: \t{unitSwitchDuration}")
        print(f"Unit Gradient Duration: {unitGradientDuration}")
        print(f"Unit Change Mode: \t{unitChangeMode}")
        print(f"Hue: \t\t\t{hue}")
        print(f"Saturation: \t\t{saturation}")
        print(f"Brightness: \t\t{brightness}")
        print(f"Padding: \t\t{padding}\n")

    return effectSets


def createSet(numSet):
    print(f"\n\n\n----------")
    fullStr = ""
    for set in range(0, numSet):
        print(f"\nSet #{set+1}:")
        sceneNum = int(input("  Scene Number (0-255): "))
        unitSwitchDuration = int(input("  Unit Switch Duration (0-255): "))
        unitGradientDuration = int(input("  Unit Gradient Duration (0-255): "))
        unitChangeMode = int(
            input("  Unit Change Mode (1 - Static, 2 - Jump, 3 - Breathing): ")
        )
        hue = int(input("  Hue (0-360): "))
        saturation = int(input("  Saturation (0-1000): "))
        brightness = int(input("  Brightness (0-1000): "))
        padding = 0
        setStr = f"{hex(sceneNum)[2:].zfill(bytesSeperator[0])}{hex(unitSwitchDuration)[2:].zfill(bytesSeperator[1])}{hex(unitGradientDuration)[2:].zfill(bytesSeperator[2])}{hex(unitChangeMode)[2:].zfill(bytesSeperator[3])}{hex(hue)[2:].zfill(bytesSeperator[4])}{hex(saturation)[2:].zfill(bytesSeperator[5])}{hex(brightness)[2:].zfill(bytesSeperator[6])}{hex(padding)[2:].zfill(bytesSeperator[7])}"
        #
        fullStr += setStr
    fullStr += "00"
    print(f"\n\n{fullStr}\n\n")
    return fullStr


while True:
    choice = int(input(f"Choose:\n1: Decode\n2: Create new sets\n3: Quit\n"))
    if choice == 1:
        strToDecode = input("Input string to decode: ")
        decode(strToDecode)
    elif choice == 2:
        numSet = int(input("How many sets to create? "))
        createSet(numSet)
    elif choice == 3:
        break
    else:
        print("Invalid choice.")
