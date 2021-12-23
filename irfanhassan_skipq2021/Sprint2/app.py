#!/usr/bin/env python3
import os

from aws_cdk import core as cdk

# For consistency with TypeScript code, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core

#from irfan_skip_q_project1.irfan_skip_q_project1_stack import IrfanSkipQProject1Stack
from irfan_skip_q_project1.irfan_skipq_pipeline_stack import IrfanSkipQPpielineStack

app = core.App()
IrfanSkipQPpielineStack(app, "IrfanSkipQPpielineStack",env=core.Environment(account='315997497220', region='us-east-2'))
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    #env=core.Environment(account='123456789012', region='us-east-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    

app.synth()
    
    
    
    
    
    