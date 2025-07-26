def encoding(text , shift):
    encode = ""
    for i in text: 
        if i.isupper() or i.islower():
            encode += chr(ord(i) + shift)
        else:
            encode += " "
    return encode


def decoding(encoding_text , shift):
    decode = ""
    for j in encoding_text: 
        if j.isupper() or j.islower():
            decode += chr(ord(j) - shift)
        else:
            decode += " "
    return decode


text = input("Enter a text to en & decoding :")
shift = int(input())

encoding_text = encoding(text , shift)
decoding_text = decoding(encoding_text , shift)

print("Encoded text is :" ,encoding_text)
print("Decoded text is :", decoding_text)
