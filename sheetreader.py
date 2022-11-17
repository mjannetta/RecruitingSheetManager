import gspread

sa = gspread.service_account()

sh = sa.open("Lax Sort Test")

responses = sh.worksheet("Sheet1")

def get_player_info(line):
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


class player:
    info = ["First Name", "Last Name", "Phone Number", "Admission Status", "Grad Year", "High School", "City", "State",
            "Position", "Highlight Tape "]

    def __init__(self, info, contacted):
        self.info = info
        self.contacted = contacted

    @classmethod
    def string(self):
        player_string = "Player Info:\nName: " + str(info[1]) + ", " + str(info[0]) + "\nPosition: " + str(
            info[8]) + "\nPhone Number: " + str(info[2]) + "\nAdmission Status: " + str(
            info[3]) + "\nHS Grad Class: " + str(info[4]) + "\nHigh School: " + str(info[5]) + "\nHometown: " + str(
            info[6]) + ", " + str(info[7]) + "\nEmail: " + str(info[10]) + "\nIntended Major: " + str(
            info[11]) + "\nHighlight Tape: " + str(info[9])
        return player_string

line = input("Enter Line: ")
info = get_player_info(line)
test = player(info, False)
print(test.string())
