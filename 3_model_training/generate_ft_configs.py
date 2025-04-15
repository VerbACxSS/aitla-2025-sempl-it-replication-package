import yaml

CONFIGS = [
    # proofreading
    {
        'name': 'proofreading',
        'train_dataset_name': 'proofreading_train',
        'eval_dataset_name': 'proofreading_val',
        'output_dir': 'output/proofreading',
        'base_model': 'unsloth/Qwen2.5-7B-Instruct-bnb-4bit',
        'hub_model_id': 'VerbACxSS/sempl-it-proofreading-bnb',
    },
    # lex
    {
        'name': 'lex',
        'train_dataset_name': 'lex_train',
        'eval_dataset_name': 'lex_val',
        'output_dir': 'output/lex',
        'base_model': 'unsloth/Qwen2.5-7B-Instruct-bnb-4bit',
        'hub_model_id': 'VerbACxSS/sempl-it-lex-bnb',
    },
    # connectives
    {
        'name': 'connectives',
        'train_dataset_name': 'connectives_train',
        'eval_dataset_name': 'connectives_val',
        'output_dir': 'output/connectives',
        'base_model': 'unsloth/Qwen2.5-7B-Instruct-bnb-4bit',
        'hub_model_id': 'VerbACxSS/sempl-it-connectives-bnb',
    },
    # expressions
    {
        'name': 'expressions',
        'train_dataset_name': 'expressions_train',
        'eval_dataset_name': 'expressions_val',
        'output_dir': 'output/expressions',
        'base_model': 'unsloth/Qwen2.5-7B-Instruct-bnb-4bit',
        'hub_model_id': 'VerbACxSS/sempl-it-expressions-bnb',
    },
    # sentence-splitter
    {
        'name': 'sentence-splitter',
        'train_dataset_name': 'sentence_splitter_train',
        'eval_dataset_name': 'sentence_splitter_val',
        'output_dir': 'output/sentence-splitter',
        'base_model': 'unsloth/Qwen2.5-7B-Instruct-bnb-4bit',
        'hub_model_id': 'VerbACxSS/sempl-it-sentence-splitter-bnb',
    },
    # nominalizations
    {
        'name': 'nominalizations',
        'train_dataset_name': 'nominalizations_train',
        'eval_dataset_name': 'nominalizations_val',
        'output_dir': 'output/nominalizations',
        'base_model': 'unsloth/Qwen2.5-7B-Instruct-bnb-4bit',
        'hub_model_id': 'VerbACxSS/sempl-it-nominalizations-bnb',
    },
    # verbs
    {
        'name': 'verbs',
        'train_dataset_name': 'verbs_train',
        'eval_dataset_name': 'verbs_val',
        'output_dir': 'output/verbs',
        'base_model': 'unsloth/Qwen2.5-7B-Instruct-bnb-4bit',
        'hub_model_id': 'VerbACxSS/sempl-it-verbs-bnb',
    },
    # sentence-reorganizer
    {
        'name': 'sentence-reorganizer',
        'train_dataset_name': 'sentence_reorganizer_train',
        'eval_dataset_name': 'sentence_reorganizer_val',
        'output_dir': 'output/sentence-reorganizer',
        'base_model': 'unsloth/Qwen2.5-7B-Instruct-bnb-4bit',
        'hub_model_id': 'VerbACxSS/sempl-it-sentence-reorganizer-bnb',
    }
]

if __name__ == "__main__":
    with open('config_template.yaml', 'r') as file:
        config = yaml.safe_load(file)

    for CONFIG in CONFIGS:
        config['model_name_or_path'] = CONFIG['base_model']
        config['dataset'] = CONFIG['train_dataset_name']
        config['eval_dataset'] = CONFIG['eval_dataset_name']
        config['output_dir'] = CONFIG['output_dir']
        config['hub_model_id'] = CONFIG['hub_model_id']

        with open(f'configs/config_{CONFIG["name"]}.yml', 'w') as file:
            yaml.dump(config, file)
