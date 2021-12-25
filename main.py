
from ui import Ui
from evaluator import Evaluator

teacher = Evaluator()
window = Ui( teacher=teacher.judge )


window.mainloop()