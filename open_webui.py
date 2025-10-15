"""
OpenWebUI + Lorica.ai Integration Pipe

This pipe enables secure integration between OpenWebUI and Lorica.ai's encrypted
inference service using OHTTP (Oblivious HTTP) protocol.

Security Features:
- End-to-end encryption using Lorica OHTTP
- Confidential computing protection during inference
- Secure transport over HTTPS + OHTTP
- Encrypted storage within Lorica infrastructure
- Replay protection built into OHTTP protocol

Author: Alhassan Khedr
Version: 1.0.0
License: MIT
"""

from pydantic import BaseModel, Field
import os, json
from lorica import ohttp

# Create a single encrypted session using Lorica OHTTP.
# This session handles encapsulation, transport encryption, and replay protection.
encrypted_session = ohttp.Session()


class Pipe:
    """
    Lorica OHTTP Pipe for Open WebUI.

    Responsibilities:
      - Provide user-configurable parameters (Valves).
      - Encrypt and securely forward chat completion requests
        to Lorica.ai’s /chat/completions endpoint.
      - Return either a streaming iterator or a full JSON response.
      - Guarantee data confidentiality during transport, storage, and compute.

    Security lifecycle:
      1. Local encryption with OHTTP before leaving the user environment.
      2. Secure transport over HTTPS + OHTTP.
      3. Confidential computing enclaves protect data during execution.
      4. Encrypted storage within Lorica infrastructure ensures persistence safety.
    """

    class Valves(BaseModel):
        """
        Configuration options ("valves") exposed to the user in Open WebUI.
        These must be set for the Pipe to work.
        """

        LORICA_API_BASE_URL: str = Field(
            default="",
            description="Base URL for accessing Lorica API endpoints (e.g., https://api.lorica.ai/v1).",
        )
        LORICA_API_KEY: str = Field(
            default="",
            description="API key for authenticating requests to the Lorica API.",
        )
        MODEL_ID: str = Field(
            default="",
            description="Unique identifier of the model (e.g., org/model-name on Hugging Face).",
        )

    def __init__(self):
        # Initialize with empty/default valves
        self.valves = self.Valves()

    def pipe(self, body: dict, __user__: dict):
        """
        Encrypts and forwards a chat completion request to Lorica.ai.

        Args:
            body (dict): The request payload from Open WebUI
                         (e.g., {"messages": [...], "stream": true}).
            __user__ (dict): Information about the current user
                             (not used here, but provided by Open WebUI).

        Returns:
            - If `body["stream"] == True`: an iterator of streaming lines.
            - If `body["stream"] == False`: the parsed JSON response.
            - On error: a string containing the error message.

        Security Notes:
            - MODEL_ID set in Valves overrides any `model` provided in the body.
            - Data is protected at every stage:
                * Transport: OHTTP + HTTPS encryption
                * Storage: Encrypted persistence in Lorica
                * Compute: Confidential Computing enclaves ensure
                  that even during execution, plaintext is never exposed.
        """
        print(f"pipe:{__name__}")  # Debug log (safe; does not print payloads)

        # HTTP headers (authorization + content type)
        headers = {
            "Authorization": f"Bearer {self.valves.LORICA_API_KEY}",
            "Content-Type": "application/json",
        }

        # Payload: merge input body with configured model and enforce streaming
        payload = {
            **body,
            "model": self.valves.MODEL_ID,
            "stream": True,
        }

        try:
            # Send request securely through OHTTP session
            r = encrypted_session.post(
                url=f"{self.valves.LORICA_API_BASE_URL}/v1/chat/completions",
                json=payload,
                headers=headers,
                stream=True,
            )

            # Raise error if HTTP response code indicates failure (4xx/5xx)
            r.raise_for_status()

            # Return streaming iterator if requested
            if body.get("stream", False):
                return r.iter_lines()
            else:
                # Otherwise return full JSON response
                return r.json()

        except Exception as e:
            # Return safe error message (no secrets leaked)
            return f"Error: {e}"
