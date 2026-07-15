def fazan(char_len, *cuvinte):
    for i in range(len(cuvinte)-1):
        cuvant_curent = cuvinte[i]
        cuvant_urm = cuvinte[i+1]
        final_curent = cuvant_curent[-char_len:]
        inceput_urm = cuvant_urm[:char_len]
        if final_curent != inceput_urm:
            return False

    return True

print(fazan(2, "fazan", "antic", "icre", "rege"))
print(fazan(2, "masina", "antic", "icre", "rege"))