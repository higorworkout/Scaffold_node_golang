import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';

export class {{projectNamePascalCase}}Stack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Infrastructure resources will be added via Forge presets.
  }
}