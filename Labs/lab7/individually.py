'''
Zengping Xu
CS 5001 Fall 2020

This program can encrypt and decrypt code
'''


msg_1 = "*.glygo rsvvmw'w gshi avmxiw gsqqirxw efsyx *lmq"
# msg_1_decode = "chuck norris's code writes comments about *him*."

msg_2 = "aqwuvwem, kp cp kphkpkvg nqqr, ykvj"
# msg_2_decode = "youstuck, in an infinite loop, with"

msg_3 = ".sjajw ywzxy f htruzyjw dtz hfs’y ymwtb tzy f bnsitb.."
# msg_3_decode = "never trust a computer you can’t throw out a window..."

msg_4 = "yko.vjg swguvkqp qh yjgvjgt eqorwvgtu ecp vjkpm ku nkmg vjg swguvkqp qhyjgvjgt uwdoctkpgu ecp u"
# msg_4_decode = "the question of whether computers can think is like the question ofwhether submarines can swim."

msg_5 = ".ejwem pqttku ytkvgu dqqngcp gzrtguukqpu vjcv ctg dqvj vtwg cpf hcnug"
# msg_5_decode = "chuck norris writes boolean expressions that are both true and false."


def encrypt_shift(msg, pos):
    min_shift = 0
    max_shift = 25
    min_ord = 97
    max_ord = 122
    new_msg = ""
    if pos >= min_shift and pos <= max_shift:
        for item in msg:
            if item.isalpha():
                new_ord = ord(item) + pos
                if new_ord > max_ord:
                    new_ord = new_ord - max_ord + min_ord - 1
                new_char = chr(new_ord)
            else:
                new_char = item
            new_msg += new_char
    return new_msg


def decrypt_shift(msg, pos):
    min_shift = 0
    max_shift = 25
    min_ord = 97
    max_ord = 122
    new_msg = ""
    if pos >= min_shift and pos <= max_shift:
        for item in msg:
            if item.isalpha():
                new_ord = ord(item) - pos
                if new_ord < min_ord:
                    new_ord = new_ord + max_ord - min_ord + 1
                new_char = chr(new_ord)
            else:
                new_char = item
            new_msg += new_char
    return new_msg


def encrypt_slide(msg, pos):
    new_msg = ""
    for i in range(len(msg)):
        new_msg += msg[i - pos]
    return new_msg


def decrypt_slide(msg, pos):
    new_msg = ""
    for i in range(len(msg)):
        new_msg += msg[i - len(msg) + pos]
    return new_msg


def main():
    lst_msg = [msg_1, msg_2, msg_3, msg_4, msg_5]
    for msg in lst_msg:
        for i in range(1, 6):
            new_msg = decrypt_shift(msg, i)
            print("i", i, " ", new_msg)
            for j in range(1, 6):
                f_msg = decrypt_slide(new_msg, j)
                print("j", j, " ", f_msg)


if __name__ == "__main__":
    main()
