# # import re

# # def split_text_into_verses(text):
# #     # Regular expression to match verse numbers (numbers at the beginning of lines)
# #     verses = re.split(r'(?<=\d)\s', text)
# #     # Filter out any empty strings and strip leading/trailing whitespace
# #     verses = [verse.strip() for verse in verses if verse.strip()]
# #     return verses

# # # Example text
# # text = """God’s Final Word: His Son
# # 1 In the past God spoke to our ancestors through the prophets at many times and in various ways, 2 but in these last days he has spoken to us by his Son, whom he appointed heir of all things, and through whom also he made the universe. 3 The Son is the radiance of God’s glory and the exact representation of his being, sustaining all things by his powerful word. After he had provided purification for sins, he sat down at the right hand of the Majesty in heaven. 4 So he became as much superior to the angels as the name he has inherited is superior to theirs.

# # The Son Superior to Angels
# # 5 For to which of the angels did God ever say,

# # “You are my Son;
# #     today I have become your Father”[a]?

# # Or again,

# # “I will be his Father,
# #     and he will be my Son”[b]?

# # 6 And again, when God brings his firstborn into the world, he says,

# # “Let all God’s angels worship him.”[c]

# # 7 In speaking of the angels he says,

# # “He makes his angels spirits,
# #     and his servants flames of fire.”[d]

# # 8 But about the Son he says,

# # “Your throne, O God, will last for ever and ever;
# #     a scepter of justice will be the scepter of your kingdom.
# # 9 You have loved righteousness and hated wickedness;
# #     therefore God, your God, has set you above your companions
# #     by anointing you with the oil of joy.”[e]

# # 10 He also says,

# # “In the beginning, Lord, you laid the foundations of the earth,
# #     and the heavens are the work of your hands.
# # 11 They will perish, but you remain;
# #     they will all wear out like a garment.
# # 12 You will roll them up like a robe;
# #     like a garment they will be changed.
# # But you remain the same,
# #     and your years will never end.”[f]

# # 13 To which of the angels did God ever say,

# # “Sit at my right hand
# #     until I make your enemies
# #     a footstool for your feet”[g]?

# # 14 Are not all angels ministering spirits sent to serve those who will inherit salvation?"""

# # # Split the text into verses
# # verses = split_text_into_verses(text)
# # print(verses)
# # # Print the result
# # # for i, verse in enumerate(verses, start=1):
# # #     print(f"Verse {i}: {verse}")

# word = "\\nword"
# print(word)
# if "\\n" in word:
#     print("found")
#     splittedWord  = word.split("\\n")
#     joinedWord = ''.join(splittedWord)
#     # print(splittedWord)
#     print(joinedWord)
# else: print("not found")
word = ''''Ba ŋääø ni O Jwøk anø öö, ni mooc
øøni ka acaara ki man ŋääø ŋata näk
adïëri. Ni ø ena ri ŋata näk adïëri ki
køør Wääde ma Jecu Krictø. Manøgø
beeye Jwøk mana näk adïëri ni näk
kwøw mana näk adïëri mo bäŋ cuŋŋe. 
21 U ni therø, bëëdu ni karu bäär ki gïï
wø lam jaak.'''
print(word)
if '\n' in word:
    print("found")
    splittedWord  = word.split("\n")
    joinedWord = ' '.join(splittedWord)
    # print(splittedWord)
    print(joinedWord)