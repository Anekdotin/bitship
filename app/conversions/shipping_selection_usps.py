

def shipping_box_type(selected_shipping_choices):

    if selected_shipping_choices == 7:
        # letter
        the_length = 9
        the_width = 1
        the_height = 4

        the_weight = 1

    elif selected_shipping_choices == 8:
        # Flat Rate Envolope Letter

        the_length = 12
        the_height = 9
        the_width = 1
        the_weight = 1

    elif selected_shipping_choices == 9:
        # Flat Rate Envolope Legal

        the_length = 12
        the_width = 9
        the_height = 1

        the_weight = 1

    elif selected_shipping_choices == 10:
        # Flat Rate Envolope Padded

        the_length = 12
        the_width = 9
        the_height = 1

        the_weight = 1

    elif selected_shipping_choices == 11:
        # Flat Rate Envolope Small

        the_length = 10
        the_width = 6
        the_height = 1

        the_weight = 1

    elif selected_shipping_choices == 12:
        # Flat Rate Envolope Window

        the_length = 5
        the_width = 10
        the_height = 1

        the_weight = 1

    elif selected_shipping_choices == 13:
        # Flat Rate Envolope Gift Card

        the_length = 10
        the_width = 7
        the_height = 1

        the_weight = 1

    elif selected_shipping_choices == 14:
        # Flat Rate Envolope CardBoard

        the_length = 15
        the_width = 9
        the_height = 1

        the_weight = 1

    elif selected_shipping_choices == 15:
        # Flat Rate Box Small

        the_length = 9
        the_width = 6
        the_height = 2

        the_weight = 10

    elif selected_shipping_choices == 16:
        # Flat Rate Box Medium

        the_length = 12
        the_width = 8
        the_height = 6

        the_weight = 10

    elif selected_shipping_choices == 17:
        # Flat Rate Box Large

        the_length = 12
        the_width = 12
        the_height = 6

        the_weight = 10

    elif selected_shipping_choices == 18:
        # Flat Rate Box Large Board Game

        the_length = 24
        the_width = 12
        the_height = 3

        the_weight = 10

    else:
        the_length = 24
        the_width = 12
        the_height = 3

        the_weight = 10

    return the_length, the_width, the_height, the_weight
