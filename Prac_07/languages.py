from Prac_07.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(ruby, "\n", python, "\n", visual_basic)

languageList = [ruby, python, visual_basic]

print("The dynamically typed languages are:")

for item in languageList:
    if item.is_dynamic() == True:
        print(item.name)
    else:
        pass
