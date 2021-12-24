from aws_cdk import (
    core as cdk,
    pipelines,
    aws_codepipeline_actions as cpactions
)
from irfan_skip_q_project1.irfan_skip_q_project1_stage import IrfanSkipQPpielineStage

class IrfanSkipQPpielineStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        ###### source ########################
        source = pipelines.CodePipelineSource.git_hub(repo_string = "muhammadskipq2021/ProximaCentauri",branch = "main",
                           authentication = cdk.SecretValue.secrets_manager("Irfan_sprint2_secretkey"),
                           trigger = cpactions.GitHubTrigger.POLL)
                           
        synth = pipelines.ShellStep('synth', input= source,
                commands = ["cd irfanhassan_skipq2021/Sprint1","pip install aws-cdk.aws_cloudwatch_actions==1.135.0", 
                            "pip install -r requirements.txt ","npm install -g aws-cdk","cdk synth" ],
                            primary_output_directory = "irfanhassan_skipq2021/Sprint2/cdk.out"
                            )
        pipeline = pipelines.CodePipeline(self,'pipeline',synth=synth)
        beta_stage = IrfanSkipQPpielineStage(self, "Beta_stage", env = { 'account': '315997497220', 'region': 'us-east-2'})
        #test = pipeline.ShellStep('unit_test',"cd irfanhassan_skipq2021/Sprint2", "pip install -r requirements.txt",
        #"pip install pytest", "pytest unitTest","pytest intigrationTest")
        #pipeline.add_stage(beta_stage)
        