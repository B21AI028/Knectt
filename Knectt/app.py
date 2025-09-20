# from flask import Flask, render_template, request, jsonify
# # from responses import get_response, handle_option



# def handle_option(option):
#     if option == 1:
#         return "Plz ask me your question 😊 (e.g. Office? COD? Diet Plans? Weight Loss? etc.)"
#     elif option == 2:
#         return "Plz ask me your question 🤔"
#     elif option == 3:
#         return (
#             "Open up pre-Home page with 3 options:<br>"
#             "👉 KNECTT+<br>"
#             "👉 KNECTT PREMIUM<br>"
#             "👉 DIY"
#         )
#     else:
#         return "Invalid option."
    


# def get_response(user_input):
#     user_input = user_input.lower()

#     # Option 1 (Pre-purchase questions)
#     if "office" in user_input or "where are you" in user_input or "location" in user_input:
#         return "KNECTT is registered at Amrapali Princely Estate, Sec-76, Noida, Uttar Pradesh."

#     elif "cod" in user_input or "cash on delivery" in user_input or "pay cash" in user_input:
#         return "KNECTT accepts pre-paid orders only. 💳"

#     elif "diet" in user_input or "nutrition" in user_input or "plan" in user_input:
#         return (
#             "KNECTT prepares hyper-personalized diet plan for you, every 3 days, "
#             "as per your medical history, lifestyle, eating habits, and blood tests. "
#             "🚫 No crash dieting. You also interact with a Nutritionist to fine-tune your plan."
#         )

#     elif "weight" in user_input and "loss" in user_input:
#         return (
#             "KNECTT follows WHO rules: ~500 gms of weight loss per week in a healthy way. ⚖️ "
#             "Disclaimer: Results vary depending on metabolic rate, gender, age, and motivation."
#         )

#     elif "what if i don't lose" in user_input or "not lose weight" in user_input:
#         return (
#             "Medical Disclaimer ⚠️ Results may vary person to person. "
#             "KNECTT has 16 years of applied nutrition experience with clients across 117 cities & 12 countries. "
#             "✅ If you follow our diets, you will get results."
#         )

#     elif "discount" in user_input:
#         return "All displayed products/services are pre-discounted and 100% value for money ✅."

#     elif "sample diet" in user_input:
#         return (
#             "KNECTT prepares hyper-personalized diet plans for you every 3 days. "
#             "No single-day samples available. You can interact with our Nutritionist anytime."
#         )

#     elif "when will" in user_input or "delivery" in user_input or "reach me" in user_input:
#         return (
#             "KNECTT logistics partner is Delhivery 🚚 (express mode). "
#             "Track status under 'My Orders'. Exact TAT depends on courier availability."
#         )

#     elif "fatty liver" in user_input or "diabetes" in user_input or "cholesterol" in user_input or "acidity" in user_input:
#         return (
#             "Absolutely ✅ KNECTT offers pocket-friendly 30-day plans for conditions like fatty liver, diabetes, acidity, and cholesterol. "
#             "Premium plans are available for comprehensive care."
#         )

#     elif "difference" in user_input and "premium" in user_input:
#         return (
#             "KNECTT+ = pocket nutritionist concept (short period, pocket-friendly, live chat guidance). 💬<br>"
#             "KNECTT PREMIUM = comprehensive plan with unlimited video support, break options, travel plans, and hand-picked Superfoods 🌟"
#         )

#     # Option 2 (Others → Out of scope)
#     elif "out of scope" in user_input:
#         return "We have noted your query. Allow team to come back to you. 🙏"

#     # Fallback
#     else:
#         return "We have noted your query 🤔. Our team will get back to you soon."

















# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/chat", methods=["POST"])
# def chat():
#     data = request.json
#     user_message = data.get("message", "")  # Default to empty string if message is None
#     option = data.get("option")

#     if option:  # If button option chosen
#         bot_reply = handle_option(option)
#     else:  # Free text
#         if user_message.strip():  # Only process non-empty messages
#             bot_reply = get_response(user_message)
#         else:
#             bot_reply = "Please type a message or select an option."

#     return jsonify({"reply": bot_reply})

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request, jsonify

def handle_option(option):
    if option == 1:
        return "Plz ask me your question 😊 (e.g. Office? COD? Diet Plans? Weight Loss? etc.)"
    elif option == 2:
        return "Plz ask me your question 🤔"
    elif option == 3:
        return (
            "Open up pre-Home page with 3 options:<br>"
            "👉 KNECTT+<br>"
            "👉 KNECTT PREMIUM<br>"
            "👉 DIY"
        )
    else:
        return "Invalid option."

def get_response(user_input):
    user_input = user_input.lower()

    if "office" in user_input or "where are you" in user_input or "location" in user_input:
        return "KNECTT is registered at Amrapali Princely Estate, Sec-76, Noida, Uttar Pradesh."

    elif "cod" in user_input or "cash on delivery" in user_input or "pay cash" in user_input:
        return "KNECTT accepts pre-paid orders only. 💳"

    elif "diet" in user_input or "nutrition" in user_input or "plan" in user_input:
        return (
            "KNECTT prepares hyper-personalized diet plan for you, every 3 days, "
            "as per your medical history, lifestyle, eating habits, and blood tests. "
            "🚫 No crash dieting. You also interact with a Nutritionist to fine-tune your plan."
        )

    elif "weight" in user_input and "loss" in user_input:
        return (
            "KNECTT follows WHO rules: ~500 gms of weight loss per week in a healthy way. ⚖️ "
            "Disclaimer: Results vary depending on metabolic rate, gender, age, and motivation."
        )

    elif "what if i don't lose" in user_input or "not lose weight" in user_input:
        return (
            "Medical Disclaimer ⚠️ Results may vary person to person. "
            "KNECTT has 16 years of applied nutrition experience with clients across 117 cities & 12 countries. "
            "✅ If you follow our diets, you will get results."
        )

    elif "discount" in user_input:
        return "All displayed products/services are pre-discounted and 100% value for money ✅."

    elif "sample diet" in user_input:
        return (
            "KNECTT prepares hyper-personalized diet plans for you every 3 days. "
            "No single-day samples available. You can interact with our Nutritionist anytime."
        )

    elif "when will" in user_input or "delivery" in user_input or "reach me" in user_input:
        return (
            "KNECTT logistics partner is Delhivery 🚚 (express mode). "
            "Track status under 'My Orders'. Exact TAT depends on courier availability."
        )

    elif "fatty liver" in user_input or "diabetes" in user_input or "cholesterol" in user_input or "acidity" in user_input:
        return (
            "Absolutely ✅ KNECTT offers pocket-friendly 30-day plans for conditions like fatty liver, diabetes, acidity, and cholesterol. "
            "Premium plans are available for comprehensive care."
        )

    elif "difference" in user_input and "premium" in user_input:
        return (
            "KNECTT+ = pocket nutritionist concept (short period, pocket-friendly, live chat guidance). 💬<br>"
            "KNECTT PREMIUM = comprehensive plan with unlimited video support, break options, travel plans, and hand-picked Superfoods 🌟"
        )

    elif "out of scope" in user_input:
        return "We have noted your query. Allow team to come back to you. 🙏"

    else:
        return "We have noted your query 🤔. Our team will get back to you soon."


# Flask app
app = Flask(__name__)

@app.route("/")
def index():
    return "✅ Chatbot API is running. Use POST /chat endpoint."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    option = data.get("option")

    if option:
        bot_reply = handle_option(option)
    else:
        if user_message.strip():
            bot_reply = get_response(user_message)
        else:
            bot_reply = "Please type a message or select an option."

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    # host='0.0.0.0' makes it public, port=5000 is standard
    app.run(host="0.0.0.0", port=5000, debug=True)
