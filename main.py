import expanded_script_generator


def main():
    expanded_script_generator.generate_python_script(
        'yaml_examples/experiment-basic.yml', 
        'generated_scripts/expanded_scripts/experiment-basic.py'
    )
    expanded_script_generator.generate_python_script(
        'yaml_examples/prepare_train.yml', 
        'generated_scripts/expanded_scripts/prepare_train.py'
    )

if __name__ == '__main__':
    main()