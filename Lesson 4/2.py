def is_triange(side_a, side_b, side_c):
    """
    Decides if the triangle may exist
    """
    if side_a < side_b + side_c and side_b < side_a + side_c and side_c < side_a + side_b:
        return True
    else:
        return False

side_a = int(input('Введите длину стороны a: '))
side_b = int(input('Введите длину стороны b: '))
side_c = int(input('Введите длину стороны c: ')) 

print(is_triange(side_a, side_b, side_c))