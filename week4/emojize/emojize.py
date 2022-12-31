import emoji

emoji_in_text = input("Input: ")
print(f"Output: {emoji.emojize(emoji_in_text, language='alias')}")
