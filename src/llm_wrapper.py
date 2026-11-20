# This script generates prompts, and delegates jobs to claude_interface.py and gemma_interface.py, then interprets the results.
# Inputs are configured using the --config flag, which points to a JSON config file.
# Raw responses → /data/raw
# Processed responses → /data/processed
import argparse
import json
import os
import re
import csv
import random


def main():
    p = argparse.ArgumentParser()
    p.add_argument("-c", "--config", type=str, default="./config/config.json", help="Path to the JSON config file.")
    args = p.parse_args()
    
    config = read_config(args.config)
    
    # Dictionary mapping resume filename to a list of the processed outputs from each LLM
    claude_processed = {}
    gemma_processed = {}
    # Get list of resumes
    for resume in os.listdir(config["resume_dir"]):
        print(f"Found resume: {resume}")
        # Lists storing raw responses from each LLM for this resume
        claude_responses = []
        gemma_responses = []
        # Run each resume the specified number of times
        for i in range(config["runs_per_resume"]):
            print(f"  Round {i+1}...")
            # Delegate LLMs
            claude_responses.append(delegate_to_claude(config["prompt"], resume))
            gemma_responses.append(delegate_to_gemma(config["prompt"], resume))
        # Process responses to this resume
        claude_processed[resume] = interpret_responses(claude_responses)
        gemma_processed[resume] = interpret_responses(gemma_responses)
        # Store raw responses to this resume
        store_raw_responses(claude_responses, config["raw_dir"], "claude", resume)
        store_raw_responses(gemma_responses, config["raw_dir"], "gemma", resume)
    # Store processed responses
    store_processed_responses(claude_processed, config["processed_dir"], "claude")
    store_processed_responses(gemma_processed, config["processed_dir"], "gemma")
    
    
# Reads runtime config from config path, returns a dictionary of config parameters
def read_config(config_path):
    with open(config_path, 'r') as f:
        config = json.load(f)
        
    return config
    
            
# Delegates jobs to the Claude interface, returns response string.
def delegate_to_claude(prompt, resume):
    # !!! PLACEHOLDER !!! REPLACE ONCE INTERFACE IS WRITTEN
    return f"I, Claude, would give this candidate a score of {random.randint(1, 100)} on a scale of 1 to 100."

# Delegates jobs to the Gemma interface, returns response string.
def delegate_to_gemma(prompt, resume):
    # !!! PLACEHOLDER !!! REPLACE ONCE INTERFACE IS WRITTEN
    return f"I, Gemma, would give this candidate a score of {random.randint(1, 100)} on a scale of 1 to 100."


# Interprets raw responses from the LLM, returning the list of the interpreted values for each response. If a valid rating could not be found, a value of 0 is returned instead.
def interpret_responses(responses):
    processed = []
    for resp in responses:
        # Extract all numbers in range 1 to 100 from the response string
        numbers = [int(num) for num in re.findall(r'\d+', resp) if 1 <= int(num) <= 100]
        if len(numbers) > 0:
            processed.append(numbers[0])
        else:
            processed.append(0)
            
    return processed


# Stores raw responses from the LLM to the raw directory, with a filename indicating the resume and LLM used.
def store_raw_responses(responses, raw_dir, llm_name, resume):
    rawfile = f"{raw_dir}/{llm_name}_{os.path.splitext(resume)[0]}_raw.csv"
    with open(rawfile, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows([resp] for resp in responses)
    print(f"  Stored raw responses to {rawfile}")


# Stores processed responses to the processed directory, with a filename indicating the LLM used.
def store_processed_responses(responses, processed_dir, llm_name):
    procfile = f"{processed_dir}/{llm_name}_proc.csv"
    with open(procfile, mode="w", newline="", encoding="utf-8") as file:
        writer=csv.writer(file)
        for k, v in sorted(responses.items()):
            row = [k]
            row.extend(v)
            writer.writerow(row)
    print(f"Stored processed results to {procfile}")
    
    
if __name__ == '__main__' : main()