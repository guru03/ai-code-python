from enum import Enum

class TopicChoices(Enum):
    ANGULAR_FUNDAMENTALS = ("angular_fundamentals", "Angular Fundamentals")
    COMPONENTS_TEMPLATES = ("components_templates", "Components & Templates")
    DIRECTIVES_PIPES = ("directives_pipes", "Directives & Pipes")
    DEPENDENCY_INJECTION_SERVICES = ("dependency_injection_services", "Dependency Injection & Services")
    COMPONENT_LIFECYCLE = ("component_lifecycle", "Component Lifecycle")
    ROUTING = ("routing", "Routing")
    FORMS = ("forms", "Forms")
    HTTP_APIS = ("http_apis", "HTTP & APIs")
    RXJS = ("rxjs", "RxJS")
    SIGNALS = ("signals", "Signals")
    STATE_MANAGEMENT = ("state_management", "State Management")
    ANGULAR_MATERIAL = ("angular_material", "Angular Material")
    ADVANCED_ANGULAR = ("advanced_angular", "Advanced Angular")
    SSR_HYDRATION = ("ssr_hydration", "SSR & Hydration")
    TESTING = ("testing", "Testing")
    PERFORMANCE = ("performance", "Performance")
    SECURITY = ("security", "Security")
    BUILD_DEPLOYMENT = ("build_deployment", "Build & Deployment")
    ANGULAR_ECOSYSTEM = ("angular_ecosystem", "Angular Ecosystem")
    EXPERT_ANGULAR = ("expert_angular", "Expert Angular")

    @property
    def value_key(self) -> str:
        """Return the internal key (stored in DB)."""
        return self.value[0]

    @property
    def label(self) -> str:
        """Return the human-readable label (shown in UI)."""
        return self.value[1]

    @classmethod
    def choices(cls):
        """Return choices list for Django models."""
        return [(member.value_key, member.label) for member in cls]
