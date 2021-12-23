from aws_cdk import core as cdk

from irfan_skip_q_project1_stack import IrfanSkipQProject1Stack

class IrfanSkipQPpielineStack(cdk.Stage):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        irfan_skip_q_project1_stack =  IrfanSkipQProject1Stack(self,'IrfanSkipQProject1Stack')