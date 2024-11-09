# To-Do List Django project

This project is a **To-Do List** API developed using Django and Django Ninja, structured following **Clean Architecture** principles with strict adherence to **SOLID** principles. This architecture allows for scalability, maintainability, and testability by organizing the project into well-defined layers.

## Project Structure

The codebase is organized into four main layers, each with a specific responsibility and minimal dependencies on other layers:

- **Entities**: Core business models, which define the fundamental properties of each domain entity, such as a `Task`. Entities do not depend on other layers.
  
- **Domain**: Holds the core business logic and rules. This layer manages interactions with `Entities` and defines interfaces (repositories) to interact with the data.

- **Application**: Contains use cases that coordinate actions on `Entities` via services like `TaskManager` to handle operations such as creating, updating, or deleting tasks.

- **Infrastructure**: Implements the interfaces defined in the `Domain` layer and handles communication with the outside world (e.g., databases, external APIs). It also includes the API layer built using Django Ninja.

### Layered Structure Overview

