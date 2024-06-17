import re
import datetime
import smtplib

def calculate_discount(total):
    discount_rate = 0.1  # 10% discount
    discount = total * discount_rate
    return discount

def calculate_gst(total):
    gst_rate = 0.18  # 18% GST
    gst = total * gst_rate
    return gst

def search_item():
    with open("items.txt", "r") as f:
        txt = f.read()
        
    prices = {
        "soap": 20,
        "facewash": 15,
        "cheese": 35,
        "honey": 50,
        "wheat flour": 40,
        "maida": 40,
        "sugar": 25,
        "coffee powder": 30,
        "ketchup": 45,
        "bread": 20,
        "eggs": 6,
        "soap powder": 15,
        "chocolates": 20,
        "peanut butter": 50
    }
    
    total_final_price = 0
    bill_details = []

    while True:
        your_order = input("Enter the item you want to buy: ").lower()
        x = re.search(your_order, txt, re.IGNORECASE)

        if x:
            print(f"Yes, {your_order} is available")
            try:
                no_items = int(input(f"Enter the number of {your_order} you want: "))
                if your_order in prices:
                    total = prices[your_order] * no_items
                    
                    discount = calculate_discount(total)
                    gst = calculate_gst(total - discount)
                    final_total = total - discount + gst
                    
                    print(f"You ordered: {your_order}")
                    print(f"Your total bill before discount and GST is {total}")
                    print(f"Discount: {discount}")
                    print(f"GST: {gst}")
                    print(f"Your total bill is {final_total}")

                    total_final_price += final_total

                    current_time = datetime.datetime.now()
                    bill_details.append(f"Date & Time: {current_time}\n")
                    bill_details.append(f"You ordered: {your_order}\n")
                    bill_details.append(f"Your total bill before discount and GST is {total}\n")
                    bill_details.append(f"Discount: {discount}\n")
                    bill_details.append(f"GST: {gst}\n")
                    bill_details.append(f"Your total bill is {final_total}\n")
                    
                    print("Bill generated successfully")

                else:
                    print(f"Sorry, {your_order} is not available")
            except ValueError:
                print("Please type a number only")

            var = input("Do you want to add another item? (Yes/No): ").lower()
            if var == "no":
                break
        else:
            print(f"Sorry, {your_order} is not available")

    bill_details.append(f"Your final total bill for all items is: {total_final_price}\n")

    with open("bill.txt", "w") as f:
        for line in bill_details:
            f.write(line)

    print(f"Your final total bill for all items is: {total_final_price}")

def email_sending():
    try:
        receiver_mails = ["admin@gmail.com", "buyer@gmail.com"]  # bill is sent to supermarket admin and buyer
        for i in receiver_mails:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("admin@gmail.com", "admin_encrypted_password")
            f=open("items.txt","r")
            txt = f.read()
            message = f"Subject: Purchase Bill\n\n{txt}"
            s.sendmail("admin@gmail.com", i, message)
            s.quit()
            print("Bill is sent as mail successfully")
    except Exception as e:
        print(f"Mail not sent due to: {e}")

def main():
    print("\nWelcome to STAR Supermarket")
    search_item()
    email_sending()
    print("Thanks for visiting! \nHave a nice day...")

main()
