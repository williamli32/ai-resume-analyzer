import aws_cdk as cdk
from constructs import Construct
from aws_cdk import Duration
from aws_cdk import Stack
from aws_cdk import aws_lambda as lambda_
from aws_cdk import aws_lambda_python_alpha as lambda_python_
from aws_cdk.aws_apigateway import RestApi
from aws_cdk.aws_apigateway import LambdaIntegration


class BackendStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        api = RestApi(self, "resume-analyzer-api", rest_api_name="resume-analyzer-api")

        flask_lambda = lambda_.Function(
            self,
            "lambda_handler",
            function_name="flask-lambda",
            code=lambda_.Code.from_asset("/home/hithere1337/Projects/ai-resume-analyzer/backend/dist/lambda_code.zip"),
            handler="handler",
            runtime=lambda_.Runtime.PYTHON_3_8,
            timeout = Duration.seconds(30),
        )

        root_resource = api.root

        any_method = root_resource.add_method(
            "ANY",
            LambdaIntegration(flask_lambda)
        )
