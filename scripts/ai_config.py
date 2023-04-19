import yaml
import data
import os

class AIConfig:
    """
    A class object that contains the configuration information for the AI

    Attributes:
            purpose (str): The name of the AI.
            desired_outcomes (str): 
            suggested_procedure (list): The list of user suggested objectives the AI is supposed to complete.
    """

    def __init__(self, ai_name: str="", purpose: str="", desired_outcomes: str="", suggested_procedure: list=[]) -> None:
        """
        Initialize a class instance

        Parameters:
            purpose (str): The name of the AI.
            desired_outcomes (str): 
            suggested_procedure (list): The list of user suggested objectives the AI is supposed to complete.
        Returns:
            None
        """
        self.ai_name = ai_name
        self.purpose = purpose
        self.desired_outcomes = desired_outcomes
        self.suggested_procedure = suggested_procedure

    # Soon this will go in a folder where it remembers more stuff about the run(s)
    SAVE_FILE = os.path.join(os.path.dirname(__file__), '..', 'ai_settings.yaml')

    @classmethod
    def load(cls: object, config_file: str=SAVE_FILE) -> object:
        """
        Returns class object with parameters (ai_name, ai_role, ai_goals) loaded from yaml file if yaml file exists,
        else returns class with no parameters.

        Parameters:
           cls (class object): An AIConfig Class object.
           config_file (int): The path to the config yaml file. DEFAULT: "../ai_settings.yaml"

        Returns:
            cls (object): An instance of given cls object
        """

        try:
            with open(config_file) as file:
                config_params = yaml.load(file, Loader=yaml.FullLoader)
        except FileNotFoundError:
            config_params = {}

        ai_name = config_params.get("ai_name", "")
        purpose = config_params.get("purpose", "")
        desired_outcomes = config_params.get("desired_outcomes", [])
        suggested_procedure = config_params.get("suggested_procedure", [])

        return cls(ai_name, purpose, desired_outcomes, suggested_procedure)

    def save(self, config_file: str=SAVE_FILE) -> None:
        """
        Saves the class parameters to the specified file yaml file path as a yaml file.

        Parameters:
            config_file(str): The path to the config yaml file. DEFAULT: "../ai_settings.yaml"

        Returns:
            None
        """

        config = {"ai_name": self.ai_name, "purpose": self.purpose, "desired_outcomes": self.desired_outcomes, "suggested_procedure": self.suggested_procedure}
        with open(config_file, "w") as file:
            yaml.dump(config, file)

    def construct_full_prompt(self) -> str:
        """
        Returns a prompt to the user with the class information in an organized fashion.

        Parameters:
            None

        Returns:
            full_prompt (str): A string containing the initial prompt for the user including the ai_name, ai_role and ai_goals.
        """

        prompt_start = """Play to your strengths as an LLM and pursue simple strategies with no legal complications."""

        # Construct full prompt
        full_prompt = f"PURPOSE:\n\n{self.purpose}\n\nDESIRED OUTCOMES:\n\n"
        for i, outcome in enumerate(self.desired_outcomes):
            full_prompt += f"{i+1}. {outcome}\n"
        full_prompt += f"\n\nSUGGESTED PROCEDURE:"
        for i, step in enumerate(self.suggested_procedure):
            full_prompt += f"{i+1}. {step}\n"
        full_prompt += f"\n\n{prompt_start}"
        full_prompt += f"\n\n{data.load_prompt()}"
        return full_prompt
