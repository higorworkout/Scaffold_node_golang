import * as cdk from 'aws-cdk-lib';
import { Template } from 'aws-cdk-lib/assertions';
import { {{projectNamePascalCase}}Stack } from '../lib/{{projectName}}-stack';

test('Stack created successfully', () => {
  const app = new cdk.App();
  const stack = new {{projectNamePascalCase}}Stack(app, 'test-stack');
  const template = Template.fromStack(stack);

  template.resourceCountIs('*', 0);
});