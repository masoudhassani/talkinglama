from utils import load_configs
from langchain.llms import CTransformers


class Chatbot:
    def __init__(self) -> None:
        # load the config file
        configs = load_configs("configs.yml")

        # load the llm model
        model_name = configs["model_name"]
        self.model = self._load_model(model_name)

    def _load_model(self, model):
        try:
            llm = CTransformers(
                model=f"models/{model}",
                model_type="llama",
                config={"max_new_tokens": 256, "temperature": 0},
            )
            print("model loaded successfully")
            return llm

        except Exception as e:
            print(f"error loading /models/{model} \n{e}")
            return None

    def generate_response(self, prompt):
        response = self.model(prompt)
        return response


def main():
    chatbot = Chatbot()
    prompt = (
        "write me an email to send to a service provider to renew my internet service"
    )
    response = chatbot.generate_response(prompt)
    print(response)


if __name__ == "__main__":
    main()
