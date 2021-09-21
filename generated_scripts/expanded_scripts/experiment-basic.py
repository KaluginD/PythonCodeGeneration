import subprocess
def hello_world():
        env = {}
        inputs = {}
        outputs = {}
        script = ['echo Hello World!', 'echo "Time is $(date)"\n']

        cmdline = ' && '.join([str(s) for s in script])
        subprocess.run(cmdline, shell=True)

def train(num_iters=10, ):
        env = {}
        inputs = ['./data/']
        outputs = ['./models/default/model.pickle']
        script = ['python3 src/train.py --n ${self.params.num_iters}', 'echo Текущие пути PATH= $PATH', 'echo']

        cmdline = ' && '.join([str(s) for s in script])
        subprocess.run(cmdline, shell=True)

def prepare():
        env = {}
        inputs = ['./src/']
        outputs = ['./data/']
        script = ['python3 src/prepare.py', 'echo']

        cmdline = ' && '.join([str(s) for s in script])
        subprocess.run(cmdline, shell=True)

def predict():
        env = {'MLDEV_MODEL_PATH': '${path(self.inputs[0])}'}
        inputs = ['./models/default/model.pickle']
        outputs = ['./results/']
        script = ['$PYTHON_INTERPRETER src/predict.py', 'echo Из переменных среды: $MLDEV_MODEL_PATH\necho Из параметров этапа: ${self.env.MLDEV_MODEL_PATH}\necho\n']

        cmdline = ' && '.join([str(s) for s in script])
        subprocess.run(cmdline, shell=True)

def hello_world(): 
    runs = [hello_world, ]
    stages = []
    services = []
    
    for run in runs:
        run()

def run_prepare(): 
    runs = [prepare, ]
    stages = []
    services = []
    
    for run in runs:
        run()

def run_prepare_train(): 
    runs = [prepare, train, ]
    stages = []
    services = []
    
    for run in runs:
        run()

def run_predict(): 
    runs = [prepare, train, predict, ]
    stages = []
    services = []
    
    for run in runs:
        run()


