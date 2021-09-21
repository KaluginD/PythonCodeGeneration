from mldev.utils import prepare_experiment_command, exec_command
def prepare(size=1, needs_dvc=True, ):
        env = {}
        inputs = [src]
        outputs = [data]
        script = ['python3 src/prepare.py']

        script = prepare_experiment_command(cmdline=' && '.join([str(s) for s in script]), env=env)
        exec_command(script)

def train(needs_dvc=True, num_iters=10, ):
        env = {}
        inputs = [data/X_train.pickle data/X_dev.pickle data/X_test.pickle data/y_train.pickle data/y_dev.pickle data/y_test.pickle]
        outputs = [models/default/model.pickle]
        script = ['python3 src/train.py --n ${self.params.num_iters}']

        script = prepare_experiment_command(cmdline=' && '.join([str(s) for s in script]), env=env)
        exec_command(script)

def present_model():
        env = {'MLDEV_MODEL_PATH': '${path(self.inputs[0].get_files()[0])}'}
        inputs = [models/default/model.pickle]
        outputs = {}
        script = ['mldev run --no-commit run_model']

        script = prepare_experiment_command(cmdline=' && '.join([str(s) for s in script]), env=env)
        exec_command(script)

def pipeline(): 
    runs = [ngrok, notificationBot, prepare, tensorboard, train, present_model, ]
    stages = []
    services = []
    
    for run in runs:
        run()

def run_model(): 
    runs = [flaskController, ]
    stages = []
    services = []
    
    for run in runs:
        run()


