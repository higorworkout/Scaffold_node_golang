# vpc-eks

Projeto Terraform estruturado para múltiplos ambientes.

## Inicialização
```bash
terraform init
```

## Plan (DEV)
```bash
terraform plan -var-file=envs/dev/terraform.tfvars
```

## Apply (DEV)
```bash
terraform apply -var-file=envs/dev/terraform.tfvars
```

## Estrutura
- envs/ → variáveis por ambiente
- modules/ → módulos reutilizáveis
