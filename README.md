# ECE59500 AI Ethics Final Project

## Pipeline
```
[1] Download templates. (Jaye)                         src/fetch_templates.py
    → experiments/template/*.txt
    │
    ▼
[2] Populate templates with names. (Harshit)           src/preprocessing.py
    → experiments/resume/*.txt
    │
    ▼
[3] Run experiments. (Jaye)                            src/llm_wrapper.py
  [3.1] Prompt Claude. (Riteng)                        src/claude_interface.py
    → experiments/raw/claude_*.txt
  [3.2] Prompt Gemma. (Woosik)                         src/gemma_interface.py
    → experiments/raw/gemma_*.txt
    │
    ▼
  [3.3] Aggregate data. (Jaye)                         src/llm_wrapper.py
    → experiments/agg/*.csv
    │
    ▼
[4] Generate plots. (Jaye)                             src/plot_all.py
    → experiments/plots/*.png
```
The `setup.sh` script performs steps 1 and 2, and `run.sh` performs steps 3 and 4.


## Repo Layout

```
ECE595-hiring/
├── README.md                                     this file           
├── data/                                         experiment data
│   ├── template/                                 resume templates
│   ├── resume/                                   input resume data
│   ├── raw/                                      raw model responses
│   ├── agg/                                      aggregated output data
│   └── plots/                                    final output plots
├── src/                                          source code
│   ├── fetch_templates.py                        downloads templates from LLMHiringFairnessSG
│   ├── preprocessing.py                          populates templates with names
│   ├── llm_wrapper.py                            runs experiments and delegates LLM jobs
│   ├── claude_interface.py                       prompts Claude and reports responses
│   ├── gemma_interface.py                        prompts Gemma and reports responses
│   └── plot_all.py                               generates final output plots
├── run.sh                                        runs end-to-end pipeline
└── setup.sh                                      sets up environment and generates input data
```