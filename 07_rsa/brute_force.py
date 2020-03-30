from encrypt_rsa import decrypt

def brute_force(public_key, ciphertext, start_char, start=14000, stop=15000):
    start_cipher = [ciphertext[0]]
    _, n = public_key
    # tested 1313, 99999
    # forgot to print what brute_force() returned
    for i in range(start, stop):
        if decrypt((i, n), start_cipher) == start_char:
        #if decrypt((i, n), ciphertext).startswith(start_char):
            yield i
    return -1

if __name__ == '__main__':
    CIPHER = [84620, 66174, 66174, 5926, 9175, 87925, 54744, 54744, 65916, 79243, 39613, 9932, 70186, 85020, 70186, 5926, 65916, 72060, 70186, 21706, 39613, 11245, 34694, 13934, 54744, 9932, 70186, 85020, 70186, 54744, 81444, 32170, 53121, 81327, 82327, 92023, 34694, 54896, 5926, 66174, 11245, 9175, 54896, 9175, 66174, 65916, 43579, 64029, 34496, 53121, 66174, 66174, 21706, 92023, 85020, 9175, 81327, 21706, 13934, 21706, 70186, 79243, 9175, 66174, 81327, 5926, 74450, 21706, 70186, 79243, 81327, 81444, 32170, 53121]
    n = 100127

    # current solutions
    for pk in [14599, 31175, 47751]:
        print(pk, '-->', decrypt((pk, n), CIPHER))

    for pk in brute_force((29815, n), CIPHER, 'h', 1, 99999):
        print(pk)
        print(decrypt((pk, n), CIPHER))
