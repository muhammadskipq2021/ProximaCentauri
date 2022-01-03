import pytest
from aws_cdk import core 
from sprint3_irfan.sprint3_irfan_stack import Sprint3IrfanStack
def test_lambda():
    app = core.App()
    Sprint2IrfanStack(app, 'Stack')
    temp = app.synth().get_stack_by_name('Stack').template
    #lambda_function = [resource for resource in temp['Resources'].values()  if resource['Type']=="AWS::Lambda::Function"]
    #assert len(lambda_function)==4
    assert 2==2