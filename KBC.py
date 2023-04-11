# Create some Important Variables
Lifeline = 5
Score = 0


# Create main() function
def main():
    global Score
    # Display Welcome Message
    print("🎉🤑👑WELCOME DEAR IN OUR KAON BANEGA CAROREPATI🎉🤑👑")
    print(input("Please first enter your name:"))
    print("very very thank you, Lets start now")

    # Asking some Questions
    # Question 1
    argument = "Your first question is:\nWho is the founder of boat ?\n1.mr.elun musk           2.mr.bill gates\n3.mr.aman gupta          4.mr.gaotam adani"
    answer = "3"
    points = 5000
    ask(argument, answer, points)

    # Question 2
    argument = "Your second question is:\nWho is the ceo of google ?\n1.tarak mehta           2.mr.sundar pichayi\n3.mr.jalebi bhai          4.mr.gaotam adani"
    answer = "2"
    points = 10000
    ask(argument, answer, points)

    # Question 3
    argument = "Your third question is:\nWho is the main character of '12 fail nobel' ?\n1.ips divya tanvar           2.sushil singh\n3.ias mr.manoj sharma          4.ias shrushti jayant deshmukh"
    answer = "3"
    points = 50000
    ask(argument, answer, points)

    # Question 4
    argument = "Your fourth question is:\nWho is the CEO of tata group ?\n1.mr.ratan tata           2.mr.mukesh ambani\n3.mr.aman gupta          4.mr.bill gates"
    answer = "1"
    points = 100000
    ask(argument, answer, points)

    # Question 5
    argument = "Your fifth question is:\nWho is the current president of India?\n1.mr.jawahar lal nehru           2.mrs.Dropati murmur\n3.mr.Sardar Patel          4.Mahatma Gandhi"
    answer = "2"
    points = 200000
    ask(argument, answer, points)

    # Question 6
    argument = "Your sixth question is:\nWhat is the capital of India?\n1.bhutan           2.pakistan\n3.america          4.delhi"
    answer = "4"
    points = 1000000
    ask(argument, answer, points)

    # Question 7
    argument = "Your seventh question is:\nWhich country won the 2019 Cricket World Cup?\n1.britain          2.south africa\n3.india          4.america"
    answer = "1"
    points = 5000000
    ask(argument, answer, points)

    # Question 8
    argument = "Your eighth question is:\nwho is inventer of areoplane?\n1.mr.elon musk           2.mr.bill gates\n3.the right brothers           4.mr.gaotam adani"
    answer = "3"
    points = 10000000
    ask(argument, answer, points)

    # Question 9
    argument = "Your ninth question is:\nWhat is the name of Ram,s father?\n1.mr.kaotilya           2.mr.batasa vale\n3.mr.dasrath          4.mr.mahakaal"
    answer = "3"
    points = 50000000
    ask(argument, answer, points)

    # Question 10
    argument = "Your tenth question is:\nWho is the chief minister of uttar pradesh?\n1.modi           2.akhilesh\n3.rahul          4.yogi baba"
    answer = "4"
    points = 100000000
    ask(argument, answer, points)

    # Question 11
    argument = "Your eleventh question is:\nwhat is the national sweet of india?\n1.jalebi           2.rasgulla\n3.chhena          4.kaju katli"
    answer = "1"
    points = 500000000
    ask(argument, answer, points)

    # Question 12
    argument = "Your twelevth question is:\nWho is enventer of bulb?\n1.thomas elva edison           2.elexander agraham bel\n3.a.p.j abdul kalam        4.subhash chandra bose"
    answer = "1"
    points = 1000000000
    ask(argument, answer, points)

    # Question 13
    argument = "Which is the most powerfull contry:\n1.India          2.China\n3.USA          4.Russia"
    answer = "3"
    points = 5000000000
    ask(argument, answer, points)

    # Question 14
    argument = "Which country produces most amount of semiconductors:\n1.India          2.China\n3.USA          4.Taiwan"
    answer = "4"
    points = 10000000000
    ask(argument, answer, points)

    # Question 15
    argument = "Your first fifteenth is:\nWhat is the name of national bird of India ?\n1.banmurgi           2.gaoraya\n3.pecock          4.sparrow"
    answer = "3"
    points = 50000000000
    ask(argument, answer, points)

    # Give Points
    print(f"KBC is over now!! You have Won {Score}Rs.")


# Define Other Important Fucntions
def ask(argument, answer, points):
    global Score
    global Lifeline
    print(argument)
    user_answer = input(":- ")
    if user_answer == answer:
        print(
            f"👏💯😮👌CONGRATULATIONS👏💯😮👌\nYour answer is 💯% right\nyou have succesfully won 🎉🤑{points}🎉🤑 rupees."
        )
        Score += points
    else:
        print("😭SORRY😭\n❌Your answer is wrong.❌\nYOU LOST YOUR 5000 RUPEES.")

        a = input("Do You Want to take Lifeline: ")
        if a == "yes":
            lifeline(answer, Lifeline)
            Lifeline -= 1
        else:
            pass


def lifeline(answer, Lifeline):
    if Lifeline > 0:
        print(f"Answer no.{answer} is the correct answer.")
    else:
        print("You have no Remaining Lifeline.")


# Run our main programm
if __name__ == "__main__":
    main()
