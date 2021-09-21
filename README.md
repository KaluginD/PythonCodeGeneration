# PythonCodeGeneration
Generation of python script based on yaml description of experiment

Based on [MLDev project](https://gitlab.com/mlrep/mldev).

WIP: The repository currently contains the first draft of the project. 

The generation is based on jinja2 templates (see [GenericPipeline2_tmpl.py](https://github.com/KaluginD/PythonCodeGeneration/blob/main/template/GenericPipeline2_tmpl.py)).
They use parsed yaml experiment configuration reorganised in the following way:
```
config = {
  'BasicStage': [list of basic stages],
  'GenericPipeline': [list of generic pipelines],
}
```
Each Stage is described by its ``name, params, env, inputs, outputs, script``.

Each GenericPipeline is described by its ``name, runs, stages, services``.

#TODO: 
  1. Support of services: TensorBoardService, NgrokService, NotificationBot, ModelControllerService
  2. Processing of expressions like: ``${self.params.num_iters}, ${env.PYTHONPATH}``
  3. Processing of nested yaml structures like:
```
params:
        <<: *bandit_loop_params
        experiment:
          <<: *default_experiment
          T: 1000
          # for this pipeline we redefine some parameters
          # and use the ones from the environment
          # they will still be in the json dump
          w: ${env.w}
```
