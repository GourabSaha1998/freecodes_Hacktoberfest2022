import random

movie_name = ["anand", "drishyam", "intersteller", "gravity", "bahubali", "pushpa", "tenet", "inception", "golmaal",
              "dangal"]


def encoded(name):
    l = len(name)
    a = []
    for i in range(l):
        if name[i] == " ":
            a.append(" ")
        else:
            a.append("*")
    encode = "".join(str(x) for x in a)
    return encode


def length_movie(name):
    l = len(name)
    return l


def is_present(letter, name):
    if letter in name:
        return True
    else:
        return False


def unlock(qn, name, letter):
    name_list = list(name)
    qn_list = list(qn)
    n = len(name)
    a = []
    for i in range(n):
        if name_list[i] == " " or name_list[i] == letter:
            a.append(name[i])
        else:
            if qn_list[i] == "*":
                a.append("*")
            else:
                a.append(name[i])
    qn_new = "".join(str(x) for x in a)
    return qn_new


def user1_input(picked_movie, qn, p1name, pp1):
    not_said = True
    while not_said:
        letter = input("Enter a random letter to check whether it is present in the movie name or not:  ")
        if is_present(letter, picked_movie):
            modified_qn = unlock(qn, picked_movie, letter)
            print(modified_qn)
            d = int(input("Press 1 to guess the movie or 2 for unlock another letter: "))
            if d == 1:
                name = input("Your guess: ")
                if name == picked_movie:
                    print(p1name, "your guess is correct.")
                    pp1 = pp1 + 1
                    not_said = False

                else:
                    print("Your guess is wrong. Try again.")
        else:
            print("Your letter is not present in the movie name.")


def user2_input(picked_movie, qn, p2name, pp2):
    not_said = True
    while not_said:
        letter = input("Enter a random letter to check whether it is present in the movie name or not:  ")
        if is_present(letter, picked_movie):
            modified_qn = unlock(qn, picked_movie, letter)
            print(modified_qn)
            d = int(input("Press 1 to guess the movie or 2 for unlock another letter: "))
            if d == 1:
                name = input("Your guess: ")
                if name == picked_movie:
                    print(p2name, "your guess is correct.")
                    pp2 = pp2 + 1
                    not_said = False
                else:
                    print("Your guess is wrong. Try again.")
        else:
            print("Your letter is not present in the movie name.")


def play():
    p1name = input("Player 1, enter your name: ")
    p2name = input("Player 2, enter your name: ")
    pp1 = 0
    pp2 = 0
    turn = 0
    willing = True
    while willing:
        if turn % 2 == 0:
            print(p1name, "Your turn.")
            picked_movie = random.choice(movie_name)
            qn = encoded(picked_movie)
            c = int(input("Press 1 for length of the movie name, 2 for first & last letter or 3 for try "
                          "yourself: "))
            print("Encoded version of movie name is", qn)
            if c == 1:
                length = length_movie(picked_movie)
                print("Length of the movie name is", length)
                user1_input(picked_movie, qn, p1name, pp1)
                e = int(input("Press 1 to continue or 2 to quit: "))
                if e == 2:
                    print(p1name, "your point is", pp1)
                    print(p2name, "your point is", pp2)
                    willing = False
                    print("Thanks for playing. Have a nice day.")

            elif c == 2:
                length = length_movie(picked_movie)
                print(f"First letter of movie is {picked_movie[0]} and last letter is {picked_movie[length - 1]}")
                user1_input(picked_movie, qn, p1name, pp1)
                e = int(input("Press 1 to continue or 2 to quit: "))
                if e == 2:
                    print(p1name, "your point is", pp1)
                    print(p2name, "your point is", pp2)
                    willing = False
                    print("Thanks for playing. Have a nice day.")

            elif c == 3:
                user1_input(picked_movie, qn, p1name, pp1)
                e = int(input("Press 1 to continue or 2 to quit: "))
                if e == 2:
                    print(p1name, "your point is", pp1)
                    print(p2name, "your point is", pp2)
                    willing = False
                    print("Thanks for playing. Have a nice day.")
        else:
            print(p2name, "Your turn.")
            picked_movie = random.choice(movie_name)
            qn = encoded(picked_movie)
            c = int(input("Press 1 for length of the movie name, 2 for first & last letter or 3 for try "
                          "yourself: "))
            print("Encoded version of movie name is", qn)
            if c == 1:
                length = length_movie(picked_movie)
                print("Length of the movie name is", length)
                user2_input(picked_movie, qn, p2name, pp2)
                e = int(input("Press 1 to continue or 2 to quit: "))
                if e == 2:
                    print(p1name, "your point is", pp1)
                    print(p2name, "your point is", pp2)
                    willing = False
                    print("Thanks for playing. Have a nice day.")

            elif c == 2:
                length = length_movie(picked_movie)
                print(f"First letter of movie is {picked_movie[0]} and last letter is {picked_movie[length - 1]}")
                user2_input(picked_movie, qn, p2name, pp2)
                e = int(input("Press 1 to continue or 2 to quit: "))
                if e == 2:
                    print(p1name, "your point is", pp1)
                    print(p2name, "your point is", pp2)
                    willing = False
                    print("Thanks for playing. Have a nice day.")

            elif c == 3:
                user2_input(picked_movie, qn, p2name, pp2)
                e = int(input("Press 1 to continue or 2 to quit: "))
                if e == 2:
                    print(p1name, "your point is", pp1)
                    print(p2name, "your point is", pp2)
                    willing = False
                    print("Thanks for playing. Have a nice day.")
        turn = turn + 1


play()
