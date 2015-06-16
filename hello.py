import sys

lang = "English"

if (len(sys.argv) > 1):
    lang = sys.argv[1]

if (lang == "English"):
    print ("Hello world!")

elif (lang == "Arabic"):
    print ("مرحبا أيها العالم!")

elif (lang == "Japanese"):
    print ("こんにちは世界！")

elif (lang == "French"):
    print ("Bonjour le monde!")

elif (lang == "Chinese"):
    print ("你好世界！")

elif (lang == "Zulu"):
    print ("Sawubona Mhlaba!")

else:
    raise RuntimeError("This shouldn't happen!")
