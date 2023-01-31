def get_user_info():

    name = {}

    name['username'] = input("What is your name: ")

    scores = {"ICT":False, "Maths":False, "Chemistry":False}

    for item in scores:

        while not scores[item]:

            score_out = input(f"{item} Score 1-100: ")

            try:
                score_out = int(score_out)
                if score_out < 0 or score_out > 100:
                    print("Incorrect range")
                    continue

                scores[item] = score_out
                print(f"You scored {score_out} %")

            except:

                print("Incorrect score")

    output = {**name, **scores}

    return output

