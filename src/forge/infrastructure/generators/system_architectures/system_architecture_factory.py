from forge.domain.system_architecture import SystemArchitecture
from forge.application.ports.system_architecture_generator import SystemArchitectureGenerator

from forge.infrastructure.system_architectures.monolith_generator import MonolithGenerator
from forge.infrastructure.system_architectures.modular_monolith_generator import ModularMonolithGenerator
from forge.infrastructure.system_architectures.microservices_generator import MicroservicesGenerator
from forge.infrastructure.system_architectures.single_microservice_generator import SingleMicroserviceGenerator


def get_system_generator(architecture: SystemArchitecture) -> SystemArchitectureGenerator:
    if architecture == SystemArchitecture.MONOLITH:
        return MonolithGenerator()

    if architecture == SystemArchitecture.MODULAR_MONOLITH:
        return ModularMonolithGenerator()

    if architecture == SystemArchitecture.MICROSERVICES:
        return MicroservicesGenerator()

    if architecture == SystemArchitecture.SINGLE_MICROSERVICE:
        return SingleMicroserviceGenerator()

    raise ValueError(f"Unsupported system architecture: {architecture}")