import hashlib
import itertools

# النص المشفر في الملف الثاني
encrypted_text = "¤ð´éÙÜÉÎĵĻġĭđĚōŹ±¾¥¯ÍÖÙrzgiY@@FdqySR["

# تقسيم النص إلى أجزاء بطول 8
chunks = [encrypted_text[i:i+8] for i in range(0, len(encrypted_text), 8)]

# جرب جميع الترتيبات الممكنة
for perm in itertools.permutations(chunks):
    encrypted = ''.join(perm)
    decrypted = ''
    
    # فك التشفير باستخدام XOR
    for i in range(40):
        decrypted += chr(ord(encrypted[i]) ^ (i << 3))
    
    # التحقق من MD5
    if hashlib.md5(decrypted[:39].encode()).hexdigest() == "ac9dc5b77c199d4737f5010da0fcdd24":
        print("النص الأصلي هو:", decrypted[:39])
        break