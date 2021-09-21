import yaml
from jinja2 import Environment, FileSystemLoader
from mldev.experiment import GenericPipeline, BasicStage
from mldev_dvc.dvc_stage import Stage
from mldev_config_parser import config_parser


def check_if_stage(obj):
    return 'Stage' in str(type(obj))


def generate_python_script(config, path_to_save):
    mldev_settings = config_parser.MLDevSettings()
    cfg = yaml.load(open(config, "r+"), Loader=yaml.Loader)
    
    basic_stages = []
    cfg_per_type = {'GenericPipeline': []}
    for name, value in cfg.items():
        if check_if_stage(value):
            basic_stages.append(value)
        if isinstance(value, GenericPipeline):
            curr_stage = {'name': name, 'value': value.__dict__}
            cfg_per_type['GenericPipeline'].append(curr_stage)
            for run in value.runs:
                if check_if_stage(run):
                    basic_stages.append(run)

    basic_stages = list(set(basic_stages))  
    cfg_per_type['BasicStage'] = basic_stages

    env = Environment(loader = FileSystemLoader('template/'), trim_blocks=True, lstrip_blocks=True)
    pipeline_template = env.get_template('GenericPipeline2_tmpl.py')
    render = pipeline_template.render(cfg_per_type)

    if path_to_save is None:
        path_to_save = config.rsplit('.')[0] + '.py'
    with open(path_to_save, 'w') as f:
        print(render, file=f)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate python script based on yaml experiment description.')
    parser.add_argument("--config", type=str, help="path to config.yaml file")
    parser.add_argument("--path-to-save", type=str, help="path to save python script", default=None)
    args = parser.parse_args()
    generate_python_script(args.config, args.path_to_save)
