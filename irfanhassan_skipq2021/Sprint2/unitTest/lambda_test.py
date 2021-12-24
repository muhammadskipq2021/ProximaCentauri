import pytest
from aws_cdk import core

from irfan_skip_q_project1.irfan_skip_q_project1_stack import  IrfanSkipQProject1Stack
def test_code():
    app = core.app()
    IrfanSkipQProject1Stack(app, 'Stack')
    temp = app.synth().get_stack_by_name('Stack').template
    lambda_function = [resource for resource in temp['Resources'].values  if resource['type']=="AWS::Lambda::Function"]
    assert len(lambda_function)==2
    
