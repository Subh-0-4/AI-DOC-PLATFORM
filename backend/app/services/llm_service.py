# backend/app/services/llm_service.py

class LLMService:
    """
    Simple LLM service stub.
    You can later replace generate_text with a real call to Gemini / OpenAI.
    """

    def generate_text(self, prompt: str) -> str:
        # 🔹 This is a stub. For now, just echo prompt in a structured way.
        return f"[AI Generated]\n\n{prompt.strip()}"

    def generate_section(self, main_topic: str, section_title: str) -> str:
        """
        Used during initial project creation to generate content for each section.
        """
        prompt = (
            f"Write a clear, structured section for a document.\n"
            f"Main topic: {main_topic}\n"
            f"Section title: {section_title}\n\n"
            f"Requirements:\n"
            f"- 2–3 short paragraphs\n"
            f"- Simple and professional tone\n"
            f"- Explain the idea in a way a beginner can understand.\n"
        )
        return self.generate_text(prompt)

    def refine_text(
        self,
        original: str,
        refinement_prompt: str,
        section_title: str,
        main_topic: str,
    ) -> str:
        """
        Used when user refines an existing section with a prompt.
        """
        prompt = (
            "Refine the following document section.\n\n"
            f"Main topic: {main_topic}\n"
            f"Section title: {section_title}\n"
            f"Refinement instruction: {refinement_prompt}\n\n"
            "Original text:\n"
            f"{original}\n\n"
            "Return only the improved version, no explanations."
        )
        return self.generate_text(prompt)


llm_service = LLMService()
