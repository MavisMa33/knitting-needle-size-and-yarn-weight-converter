jp_mm = {0: 2.10, 1: 2.40, 2: 2.70, 3: 3.00, 4: 3.30, 5: 3.60, 6: 3.90, 7: 4.20, 8: 4.50, 9: 4.80, 10: 5.10, 11: 5.40, 12: 5.70, 13: 6.00, 14: 6.30, 15: 6.60}

us_mm = {0: 2.00, 1: 2.25, 2: 2.75, 3: 3.25, 4: 3.50, 5: 3.75, 6: 4.00, 7: 4.50, 8: 5.00, 9: 5.50, 10: 6.00, 10.5: 6.50, 11: 8.00, 13: 9.00, 15: 10.00, 17: 12.75, 19: 15.00, 35: 19.00, 50: 25.00}

def sort_jp_mm(jp_mm):
    sorted_jp_mm = {}
    for key in sorted(jp_mm.keys()):
        sorted_jp_mm[key] = jp_mm[key]
    return sorted_jp_mm

def sort_us_mm(us_mm):
    sorted_us_mm = {}
    for key in sorted(us_mm.keys()):
        sorted_us_mm[key] = us_mm[key]
    return sorted_us_mm

def jp_mm_converter(user_input):

    if user_input in jp_mm:
        print("Knitting needle JP size: " + str(user_input))
        return "Knitting needle size in millimeters: " + str(jp_mm[user_input]) + "mm"
   
    return "Please check the size number and try it again."

def us_mm_converter(user_input):

    if user_input in us_mm:
        print("Knitting needle US size: " + str(user_input))
        return "Knitting needle size in millimeters: " + str(us_mm[user_input]) + "mm"
   
    return "Please check the size number and try it again."

def us_jp_converter(user_input):

    sorted_jp_mm = sort_jp_mm(jp_mm)

    if user_input in us_mm:

        smallestAbs = float("inf")
        smallest_jp = []

        for jp_size in sorted_jp_mm:
            dif = abs(sorted_jp_mm[jp_size] - us_mm[user_input])
            if dif < smallestAbs:
                smallest_jp = []
                smallest_jp.append(jp_size)
                smallestAbs = dif
            elif dif == smallestAbs:
                smallest_jp.append(jp_size)
            else:
                break
        
        return "The nearest JP size is " + str(smallest_jp) + "."
    
        # compared_list = {}

        # for jp_size in jp_to_mm_lab:
        #     compared_num = abs(jp_to_mm_lab[jp_size] - us_to_mm_lab[user_input])
        #     compared_list[jp_size] = compared_num

        # for key, value in compared_list.items():
        #     if value == min(compared_list.values()):
        #         print("Knitting needle US size: " + str(user_input))
        #         return "The nearest JP size is " + str(key) + "."
    
    return "Please check the size number and try it again."

def jp_us_converter(user_input):

    sorted_us_mm = sort_us_mm(us_mm)

    if user_input in jp_mm:

        smallest_us = []
        smallestAbs = float("inf")

        for us_size in sorted_us_mm:
            dif = abs(sorted_us_mm[us_size] - jp_mm[user_input])
            if dif < smallestAbs:
                smallest_us = []
                smallest_us.append(us_size)
                smallestAbs = dif
            elif dif == smallestAbs:
                smallest_us.append(us_size)
            else:
                break
        
        return "The nearest US size is " + str(smallest_us) + "."
    
    return "Please check the size number and try it again."

