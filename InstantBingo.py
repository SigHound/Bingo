import random


# def card_set():
#     available_numbers = {}
#     keys = ['B', 'I', 'N', 'G', 'O']
#     i = 0
#     x = 0
#     for item in keys:
#         values = []
#         i += 1
#         while x < 15*i:
#             x += 1
#             values.append(x)
#             if x == 15*i:
#                 new_item = {item: values}
#                 available_numbers.update(new_item)
#     return available_numbers


# def new_card_generator():
# #     new_card = {}
# #     i = 0
# #     x = 0
# #     keys = ['B', 'I', 'N', 'G', 'O']
# #     for item in keys:
# #         values = []
# #         i += 1
# #         while x < 5*i:
# #             new_number = random_generator(15*i)
# #             if new_number not in values:
# #                 new_number = random_generator(15*i)
# #             x += 1
# #             print("newNum", new_number)
# #             if new_number not in values:
# #                 values.append(new_number)
# #                 if x == 15*i:
# #                     new_item = {item: values}
# #                     new_card.update(new_item)
# #     return new_card

def new_card_generator(keys):
    new_card = {}
    i = 1
    number_range = 15
    new_value = []
    for items in keys:
        new_number_range = i * number_range
        values = list(range(new_number_range-14, new_number_range+1))
        x = 0
        while x < 5:
            x += 1
            new_value.append(values.pop(random_generator(15-x)))
            if x == 5:
                new_column = {items: new_value}
                new_card.update(new_column)
                new_value = []
        
        i += 1
    return new_card


def random_generator(max_num):
    # print("max: ", max_num)
    return random.randint(0, max_num)


def shot_caller():
    print()


def main():                                                            
    keys = ['B', 'I', 'N', 'G', 'O']
    all_of_them = []
    the_nums = []
    cards_made = int(input("How many cards would you like?"))
    for i in range(cards_made):
        all_of_them.append(new_card_generator(keys))
    for i in range(76):
        the_nums.append(i)
    the_nums.pop(0)
    print(all_of_them)


main()
