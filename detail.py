import datetime
from mailer import sendClass as sc


class detailClass():
    user_details = []
    email_details = []
    messages = []
    base_msg = """Hi {name}! 
Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!
Team CFE
"""

    def add_user(self, name, amount, email=None):
        name = name[0].upper()+name[1:].lower()
        detail = {
            "name": name,
            'amount': amount
        }
        today_obj = datetime.date.today()
        date_txt = '{today.day}/{today.month}/{today.year}'.format(
            today=today_obj)
        detail['date'] = date_txt
        if email is not None:
            detail["email"] = email
        self.user_details.append(detail)

    def get_details(self):
        return self.user_details

    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                name = detail["name"]
                amount = detail["amount"]
                date = detail['date']
                message = self.base_msg
                new_msg = message.format(
                    name=name,
                    date=date,
                    total=amount
                )
                user_email = detail.get("email")
                if user_email:
                    user_data = {
                        "email": user_email,
                        "message": new_msg
                    }
                    self.email_details.append(user_data)
                else:
                    self.messages.append(new_msg)
            return self.messages
        return []

    def send_email(self):
        self.make_messages()
        if len(self.email_details) > 0:
            sc.set_Conn()
            for detail in self.email_details:
                user_email = detail["email"]
                user_msg = detail["message"]
                # run email
                sc.to_email = user_email
                sc.plain_txt = user_msg
                sc.send_email()
            sc.quit_email()
            print("Well!")
        return False


obj = detailClass()
sc.username = input("Enter the username: ")
num = int(input("Enter the number of receivers: "))
for i in range(0, num):
    name = input("Enter the name: ")
    amount = input("Enter the amount: ")
    email = input("Enter the mail id:")
    obj.add_user(name, amount, email=email)

print("Initiating send!")
obj.send_email()
