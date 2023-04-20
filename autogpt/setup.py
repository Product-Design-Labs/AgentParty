"""Set up the AI and its goals"""
from colorama import Fore, Style

from autogpt import utils
from autogpt.config.ai_config import AIConfig
from autogpt.logs import logger


def prompt_user() -> AIConfig:
    """Prompt the user for input

    Returns:
        AIConfig: The AIConfig object containing the user's input
    """
    ai_name = ""
    purpose = ""
    # Construct the prompt
    logger.typewriter_log(
        "Welcome to AgentParty! ",
        Fore.GREEN,
        "run with '--help' for more information.",
        speak_text=True,
    )

    logger.typewriter_log(
        "Create an AI-Assistant:",
        Fore.GREEN,
        "Enter the Purpose, Desired Outcomes, and Suggested Procedure for"
        " Agent A. Entering nothing will load defaults.",
        speak_text=True,
    )

    # Get AI Name from User
    logger.typewriter_log(
        "Name your AI: ",
        Fore.GREEN,
        "For example, 'Agent-A'")
    ai_name = utils.clean_input("AI Name: ")
    if ai_name == "":
        ai_name = "Agent_A"

    logger.typewriter_log(
        f"{ai_name} here!", Fore.LIGHTBLUE_EX, "I am at your service.", speak_text=True
    )

    # Get Purpose from User
    logger.typewriter_log(
        "Enter the Purpose of Agent A: "
        "For example, 'an AI designed to autonomously develop and run businesses",
        Fore.GREEN)
    purpose = utils.clean_input(f"{ai_name} is: ")
    if purpose == "":
        purpose = "an AI designed to autonomously develop and run businesses with the"
        " sole goal of increasing your net worth."

    # Get Desired Outcomes from User
    logger.typewriter_log(
        "Enter Desired Outcomes for Agent A (type 'done' when finished):",
        Fore.GREEN)
    desired_outcomes = []
    while True:
        outcome = utils.clean_input("Outcome: ")
        if outcome.lower() == 'done':
            break
        desired_outcomes.append(outcome)
    if not desired_outcomes:
        desired_outcomes = [
            "Increase net worth",
            "Grow Twitter Account",
            "Develop and manage multiple businesses autonomously",
        ]
    
    # Get Suggested Procedure from User
    logger.typewriter_log(
        "Enter Suggested next steps for Agent A (type 'done' when finished):",
        Fore.GREEN)
    suggested_procedure = []
    while True:
        outcome = utils.clean_input("Step: ")
        if outcome.lower() == 'done':
            break
        suggested_procedure.append(outcome)
    if not suggested_procedure:
        suggested_procedure = [
            "Read the files inside the working directory",
            "Ask the user for input",
            "Generate a plan based on the user's input",
        ]
    

    return AIConfig(ai_name, purpose, desired_outcomes, suggested_procedure)
