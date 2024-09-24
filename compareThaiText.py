import Levenshtein

text1 = "บริษัท ทกสอบ จำกัด"
text2 = "บริษัท ทดสอบ จำกัด"

similarity = Levenshtein.ratio(text1, text2)

print(f"Similarity: {similarity}")
