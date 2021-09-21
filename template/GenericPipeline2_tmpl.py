import subprocess
{# #}
{# #}

{%- for basic_stage in BasicStage -%}
def {{basic_stage['name']}}({%- for param_name, param_value in basic_stage['params'].items()-%} 
        {{param_name}}={{param_value}}, {%endfor%}):
        env = {{basic_stage['env']}}
        inputs = {{basic_stage['inputs']}}
        outputs = {{basic_stage['outputs']}}
        script = {{basic_stage['script']}}

        cmdline = ' && '.join([str(s) for s in script])
        subprocess.run(cmdline, shell=True)

{% endfor %}

{%- for pipeline in GenericPipeline -%}
def {{pipeline['name']}}(): 
    runs = [{% for run in pipeline['value']['runs'] %}{{run['name']}}, {% endfor %}]
    stages = []
    services = []
    
    for run in runs:
        run()

{% endfor %}