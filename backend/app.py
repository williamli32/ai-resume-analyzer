#!/usr/bin/env python3
import os

import aws_cdk as cdk
from aws_cdk import App, Environment

from backend.backend_stack import BackendStack

from flask import (Flask, jsonify)
import awsgi


# app = Flask(__name__)
app = cdk.App()

BackendStack(
    app,
    "ResumeAnalyzerBackend",
    env=Environment(
        region="us-east-2",
        account="711900282734"
    )
)

app.synth()
