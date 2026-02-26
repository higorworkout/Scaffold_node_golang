import * as cdk from 'aws-cdk-lib';
import { {{projectNamePascalCase}}Stack } from '../lib/{{projectName}}-stack';

const app = new cdk.App();


const env: cdk.Environment = {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
}

new {{projectNamePascalCase}}Stack(app, '{{projectName}}-stack', {
  env: env,
});