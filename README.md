# To-Do List Django project

This project is a **To-Do List** API developed using Django and Django Ninja, structured following **Clean Architecture** principles with strict adherence to **SOLID** principles. This architecture allows for scalability, maintainability, and testability by organizing the project into well-defined layers.

## Project Structure

The codebase is organized into four main layers, each with a specific responsibility and minimal dependencies on other layers:

- **Entities**: Core business models, which define the fundamental properties of each domain entity, such as a `Task`. Entities do not depend on other layers.
  
- **Domain**: Holds the core business logic and rules. This layer manages interactions with `Entities` and defines interfaces (repositories) to interact with the data.

- **Application**: Contains use cases that coordinate actions on `Entities` via services like `TaskManager` to handle operations such as creating, updating, or deleting tasks.

- **Infrastructure**: Implements the interfaces defined in the `Domain` layer and handles communication with the outside world (e.g., databases, external APIs). It also includes the API layer built using Django Ninja.

### Layered Structure Overview
```plaintext
entities < domain < application < infrastructure

## How to Use

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your_username/your_repository.git
   cd your_repository

2. Install all required packages in `Requirements` section.


### Implemented Commands

* `make app` - up application and database/infrastructure
* `make app-logs` - follow the logs in app container
* `make app-down` - down application and all infrastructure
* `make storages` - up only storages. you should run your application locally for debugging/developing purposes
* `make storages-logs` - foolow the logs in storages containers
* `make storages-down` - down all infrastructure

### Most Used Django Specific Commands

* `make migrations` - make migrations to models
* `make migrate` - apply all made migrations
* `make collectstatic` - collect static
* `make superuser` - create admin user
