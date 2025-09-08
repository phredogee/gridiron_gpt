# phredenv/cli.py
import phredenv.sports as sports

def main():
    sports.fetch_scores()

# Inside cli.py

from xonsh.built_ins import XSH

def register_aliases(debug=False):
    XSH.aliases["fetch_scores"] = lambda: print(fetch.fetch_scores(debug=debug))
    XSH.aliases["predict_game"] = lambda: print(predict.predict_outcome("DAL", "HOU", debug=debug))
