from flask import Flask, render_template, request #routig one page to anouther page
from bs4 import BeautifulSoup #Scrap data from website
# from twilio.rest import Client
import requests #for reuasting website url
import pandas #to catch data frome CSV file
import datetime as dt
app = Flask(__name__)

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
# -----------------------function to use ----------------------
def to_integer(price):
    tal = [char for char in price if char not in [",", ".", "₹"]]
    idea = "".join(tal)
    final_price = int(idea)
    return final_price

# --------------------routing from pages -------------  --------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Amezon", methods=["GET", "POST"])
def amezon():
    if request.method == "GET":
        return render_template("Amezon.html")
    else:
        url = request.form["url"]
        wanted_price = request.form["Wanted_price"]
        name = request.form["name"]
        response = requests.get(url=url, headers=header)
        soup = BeautifulSoup(response.content, "lxml")
        bhav = soup.find_all("span", {"class":"jm-heading-xs"})
        price_of_product = to_integer(bhav[0].text)
        # photo = soup.find_all("img", id="landingImage")
        if price_of_product <= to_integer(wanted_price):
            text = "You can order it now as your price is more than \n that of product price!"
        else:
            text = "We will send you SMS when your price is more than price of product!"
        try:
            with open("D:\\python\\python_project\\data.csv", mode="a") as data:
                data_files = pandas.read_csv("D:\\python\\python_project\\data.csv")
                data_dict = data_files.to_dict()
                data.write(f"{url},{name},{wanted_price}\n")
                nicknames = data_dict["nickname"]
        except:
            with open("D:\\python\\python_project\\data.csv", mode="a") as data:
                data.write("url,nickname,wanted_price\n")
                data.write(f"{url},{name},{wanted_price}\n")
            data = pandas.read_csv("D:\\python\\python_project\\data.csv")

        return render_template("Amezon.html", price_p=price_of_product, price_w=wanted_price,
                               name=name, text=text, nicknames=nicknames)

@app.route("/flipkart", methods=["GET", "POST"])
def flipkart():
    hour = str(dt.datetime.now().strftime("%H"))
    minute = str(dt.datetime.now().strftime("%M"))
    time_no = hour + minute
    print(time_no)

    nicknames = []
    if request.method == "GET":
        return render_template("flipkart.html")
    else:
        url = request.form["url"]
        wanted_price = request.form["Wanted_price"]
        name = request.form["name"]
        response = requests.get(url=url, headers=header)
        soup = BeautifulSoup(response.content, "lxml")
        bhav = soup.find_all("div", "_30jeq3 _16Jk6d")
        print(bhav)
        price_of_product = to_integer(bhav[0].text)
        photo = soup.find_all("img", class_="_2r_T1I _396QI4")
        text = "" 
        if price_of_product <= to_integer(wanted_price):
            # account_sid = 'AC19a4d59de539e5f47a49da71e50727a5'
            # auth_token = 'e14cedc8f0d3326e2903c56795804585'
            # client = Client(account_sid, auth_token)

            # message = client.messages.create(
            # from_='whatsapp:+14155238886',
            # body=f'Your Product :- {name} \n Price :- {price_of_product} \n URL :- \n{url}',
            # to='whatsapp:+917300397500'
            # )

            # print("message sended to USer")
            text = "You can order it now as your price is more than \n that of product price!"
        else:
            text = "We will send you SMS when your price is more than price of product!"

        try:
            with open("D:\\python\\python_project\\data_f.csv", mode="a") as data:
                data_files = pandas.read_csv("D:\\python\\python_project\\data_f.csv")
                data_dict = data_files.to_dict()
                data.write(f"\n{url},{name},{wanted_price}\n")
                nicknames =data_dict["nickname"]
        except:
            with open("D:\\python\\python_project\\data_f.csv", mode="a") as data:
                data.write("url,nickname,wanted_price\n")
                data.write(f"\n{url},{name},{wanted_price}\n")
            data = pandas.read_csv("D:\\python\\python_project\\data_f.csv")
            print("error")

        return render_template("flipkart.html", price_p=price_of_product, price_w=wanted_price,
                               name=name, photo=photo[0]["src"], text=text, nicknames=nicknames)

@app.route("/cu")
def cu():
    return render_template("cu.html")

if __name__ == "__main__":
    app.run(debug=True)
