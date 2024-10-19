def is_lucky_ticket(ticket_id):
    if not isinstance(ticket_id, int):
        raise TypeError("Number should be integer")
    elif len(str(ticket_id)) != 6:
        raise ValueError("Number should have 6 digits")
    else:
        ticket_id = str(ticket_id)
        first_three_sum = sum(int(i) for i in ticket_id[0:2])
        second_three_sum = sum(int(i) for i in ticket_id[3:5])

    return first_three_sum == second_three_sum