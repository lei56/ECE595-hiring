# ECE59500 AI Ethics Final Project

Welcome to our final project for ECE59500. In this project, we test whether LLMs make different hiring dicisions based on implied cultural background and gender of applicants based on their names.

Resumes used in testing are sourced from the [LLMHiringFairnessSG](https://github.com/Social-AI-Studio/LLMHiringFairnessSG) project, whose corresponding paper can be found on [arXiv](https://arxiv.org/abs/2603.05189).

## Setup
Python 3.10 or newer is required. From the repository root, run:
```
bash setup.sh
source .venv/bin/acivate
```

`setup.sh` creates the data directories (if they do not already exist), creates a virtual environment, and installs dependencies.

Before moving on, populate the `claude_api_key` field in `config.json`.

$\color{red}{\Large\textsf{!!! WARNING: MAKE SURE NOT TO PUSH YOUR CLAUDE API KEY TO THE REPOSITORY. PLEASE. !!!}}$

## Run
To run the pipeline from end-to-end, including input data generation, running the experiments, and producing the output plots, run:
```
run.sh
```

Alternatively, to do a test run:
```
run.sh -t
```

## Pipeline
The detailed steps of the pipeline as executed by `run.sh` are detailed below:
```
[1] Download templates. (Harshit)                      src/fetch_templates.py
    → data/template/*.txt
    │
    ▼
[2] Populate templates with names. (Harshit)           src/preprocessing.py
    → data/resume/*.txt
    │
    ▼
[3] Run experiments. (Jaye)                            src/llm_wrapper.py
  [3.1] Prompt Claude. (Riteng)                        src/claude_interface.py
    → data/raw/claude_*.txt
  [3.2] Prompt Gemma. (Woosik)                         src/gemma_interface.py
    → data/raw/gemma_*.txt
    │
    ▼
  [3.3] Aggregate data. (Jaye)                         src/llm_wrapper.py
    → data/processed/*.csv
    │
    ▼
[4] Generate plots. (Jaye)                             src/plot_all.py
    → data/plots/*.png
```

## Repo Layout
The contents of this repo are summarized below:
```
ECE595-hiring/
├── README.md                                     this file           
├── data/                                         experiment data
│   ├── template/                                 resume templates
│   ├── resume/                                   input resume data
│   ├── raw/                                      raw model responses
│   ├── processed/                                aggregated output data
│   └── plots/                                    final output plots
├── test/                                         data/ environment for test runs
├── src/                                          source code
│   ├── fetch_templates.py                        downloads templates from LLMHiringFairnessSG
│   ├── preprocessing.py                          populates templates with names
│   ├── llm_wrapper.py                            runs experiments and delegates LLM jobs
│   ├── claude_interface.py                       prompts Claude and reports responses
│   ├── gemma_interface.py                        prompts Gemma and reports responses
│   └── plot_all.py                               generates final output plots
├── config/                                       configuration files
│   ├── requirements.txt                          dependency file
│   ├── config.json                               runtime configuration
│   └── test.json                                 test configuration
├── setup.sh                                      sets up environment and installs dependencies
└── run.sh                                        runs end-to-end pipeline
```

