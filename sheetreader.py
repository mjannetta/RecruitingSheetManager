import gspread

sa = gspread.service_account()

sh = sa.open("Lax Sort Test")

responses = sh.worksheet("Responses")


# Recruit class with info and
class recruit:
    info = ["First Name", "Last Name", "Phone Number", "Admission Status", "Grad Year", "High School", "City", "State",
            "Position", "Highlight Tape"]

    contacted = False

    def __init__(self, info, contacted):
        self.info = info
        self.contacted = contacted

    @classmethod
    def tostring(cls):
        player_string = "Player Info:\nName: " + str(cls.info[1]) + ", " + str(cls.info[0]) + "\nPosition: " + str(
            cls.info[8]) + "\nPhone Number: " + str(cls.info[2]) + "\nAdmission Status: " + str(
            cls.info[3]) + "\nHS Grad Class: " + str(cls.info[4]) + "\nHigh School: " + str(
            cls.info[5]) + "\nHometown: " + str(
            cls.info[6]) + ", " + str(cls.info[7]) + "\nEmail: " + str(cls.info[10]) + "\nIntended Major: " + str(
            cls.info[11]) + "\nHighlight Tape: " + str(cls.info[9])
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
        highlight_tape, email, intended_major]
    return info


# Function to write recruit info to a line in their respective class file
def write_recruit(recruit, sheet, line):
    sheet.update('A' + str(line), recruit.info[0])
    sheet.update('B' + str(line), recruit.info[1])
    sheet.update('C' + str(line), recruit.info[8])
    sheet.update('D' + str(line), recruit.info[10])
    sheet.update('E' + str(line), recruit.info[2])
    sheet.update('F' + str(line), recruit.info[5])
    sheet.update('G' + str(line), recruit.info[6])
    sheet.update('H' + str(line), recruit.info[7])
    sheet.update('I' + str(line), recruit.info[9])


# Gets the total number of recruits that have filled out the sheet
def get_num_recruits():
    num_recruits = 0
    i = 1
    while responses.acell("B" + str(i)).value is not None:
        num_recruits += 1
        i += 1
    return num_recruits


'''
def update_sheet():
   num_recruits = get_num_recruits()
   for i in range(1, num_recruits):
'''
