import pytest
from aws_cdk import core
#
from sprint3_irfan.sprint3_irfan_stack import Sprint3IrfanStack
def test_dynamotdbable():
    app = core.App()
    Sprint3IrfanStack(app, 'Stack')
    temp = app.synth().get_stack_by_name('Stack').template
    dynamodb_table = [resource for resource in temp['Resources'].values()  if resource['Type']=="AWS::DynamoDB::Table"]
    print(len(dynamodb_table))
    assert len(dynamodb_table)==1  #
    