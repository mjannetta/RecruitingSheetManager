import gspread

sa = gspread.service_account()

sh = sa.open("Lax Sort Test")

responses = sh.worksheet("Responses")


# Recruit class with info and
class recruit:
    info = ["First Name", "Last Name", "Phone Number", "Admission Status", "Grad Year", "High School", "City", "State",
            "Position", "Highlight Tape "]

    contacted = False

    def __init__(self, info, contacted):
        self.info = info
        self.contacted = contacted

    @classmethod
    def string(self):
        player_string = "Player Info:\nName: " + str(self.info[1]) + ", " + str(self.info[0]) + "\nPosition: " + str(
            self.info[8]) + "\nPhone Number: " + str(self.info[2]) + "\nAdmission Status: " + str(
            self.info[3]) + "\nHS Grad Class: " + str(self.info[4]) + "\nHigh School: " + str(
            self.info[5]) + "\nHometown: " + str(
            self.info[6]) + ", " + str(self.info[7]) + "\nEmail: " + str(self.info[10]) + "\nIntended Major: " + str(
            self.info[11]) + "\nHighlight Tape: " + str(self.info[9])
        return player_string


# Gets the player information from the given line and puts it into an array
def get_recruit_info(line):
    first_name = responses.acell('B' + str(line)).value
    last_name = responses.acell('C' + str(line)).value
    phone_number = responses.acell('D' + str(line)).value
    admission_status = responses.acell('E' + str(line)).value
    grad_year = responses.acell('F' + str(line)).value
    high_school = responses.acell('H' + str(line)).value
    city = responses.acell('I' + str(line)).value
    state = responses.acell('J' + str(line)).value
    position = responses.acell('K' + str(line)).value
    highlight_tape = responses.acell('L' + str(line)).value
    email = responses.acell('M' + str(line)).value
    intended_major = responses.acell('N' + str(line)).value
    info = [
        first_name, last_name, phone_number, admission_status, grad_year, high_school, city, state, position,
        highlight_tape,
        email, intended_major]
    return info


'''def write_recruit(player, sheet):'''

num_recruits = 0
i = 1
while (responses.acell("B" + str(i)).value != None):
    num_recruits += 1
    i += 1
print(num_recruits)
