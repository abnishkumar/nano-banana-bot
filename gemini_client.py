import os
from io import BytesIO
from dotenv import load_dotenv
from PIL import Image
from google import genai
from google.genai import types


class GeminiClient:
    def __init__(self,api_key=None):
        
        os.environ["GENAI_API_KEY"] = api_key
        self.client = genai.Client()

        # prompt = (
        #     "Create a picture of my cat eating a nano-banana in a "
        #     "fancy restaurant nside the beach constellation",
        # )

        # image = Image.open("cat_image.png")

        # response = self.client.models.generate_content(
        #     model="gemini-2.5-flash-image-preview",
        #     contents=[prompt, image],
        # )

        # for part in response.candidates[0].content.parts:
        #     if part.text is not None:
        #         print(part.text)
        #     elif part.inline_data is not None:
        #         image = Image.open(BytesIO(part.inline_data.data))
        #         image.save("generated_image.png")

    def generate(self, prompt: str, uploaded_image: Image.Image = None):
        system_prompt = """
        # INSTRUCTIONS
        Generate an image according to the instructions.
        Specify in the output text the changes made to the image.
        # OUTPUT
        A generated image and a short text.
        """

        contents = [system_prompt, prompt]

        # If an image is uploaded, attach it
        if uploaded_image:
            buffer = BytesIO()
            uploaded_image.save(buffer, format="PNG")
            img_bytes = buffer.getvalue()
            contents.append(
                types.Part.from_bytes(data=img_bytes, mime_type="image/png")
            )

        response = self.client.models.generate_content(
            model="gemini-2.5-flash-image-preview",
            contents=contents
        )

        return response

# GeminiClient()