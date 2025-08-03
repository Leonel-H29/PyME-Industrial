# PyME Industrial

## Project Overview

**PyME Industrial** is a management system designed for small and medium-sized industrial companies, specifically tailored for the purchasing department of a machinery manufacturing and repair company. The main goal is to provide detailed tracking and management of material and service requests, ensuring transparency, traceability, and timely notifications to all stakeholders involved in the procurement process.

---

## Objective

The objective of this project is to streamline and automate the tracking of item and service requests within an industrial SME. The system aims to:

- Centralize the creation and management of supply and third-party service requests.
- Explicitly manage the lifecycle and state transitions of each request.
- Notify interested users automatically whenever a request changes state.
- Ensure data consistency and efficient resource usage through a unified database access layer.
- Provide a maintainable and extensible architecture using well-established design patterns.

---

## Business Context

In the industrial sector, especially in manufacturing and repair, the timely procurement of materials and services is critical. Delays or lack of information can disrupt production planning and execution. Traditionally, tracking requests relied on manual processes, emails, and spreadsheets, leading to inefficiencies, uncertainty, and duplicated work.

PyME-Industrial addresses these issues by providing a system that:

- Tracks each request through its entire lifecycle.
- Notifies all interested parties of state changes.
- Allows easy addition or removal of observers (interested users).
- Centralizes and standardizes the creation of different request types.

---

## Request Lifecycle

Each request (either for supplies or third-party services) follows a well-defined lifecycle, modeled as a state machine. The main states are:

- **REQUIRED**: The request is registered but not yet processed.
- **QUOTED**: The purchasing department is obtaining quotes from suppliers.
- **ORDERED**: A supplier has been selected and the order placed.
- **TRANSPORTED**: The supplier has dispatched the item/service.
- **RECEIVED**: The item/service has been delivered and is available.
- **CANCELED**: The request was canceled before completion.
- **REFUNDED**: The item/service was received but later returned due to issues.

Transitions between these states are triggered by user actions or external events, ensuring full traceability and control over the procurement process.

---

## Automatic Notifications

Whenever a request changes state, all interested users (observers) are automatically notified. This ensures that everyone involved is kept up-to-date, reducing delays and miscommunication. The system supports:

- Adding/removing observers at any time.
- Notifying via email (with the possibility to extend to other channels, such as WhatsApp).
- Ensuring that at least the requester is always notified by default.

---

## Centralized Request Creation

The system supports two main types of requests:

- **Supply Requests**: For materials, including product, quantity, and unit of measure.
- **Third-Party Service Requests**: For external services, including service type and provider.

A centralized factory method ensures that all requests are created with the necessary attributes and behaviors, enforcing consistency and reducing errors.

---

## Database Access

To guarantee data consistency and efficient resource usage, the system uses a singleton pattern for database access. This ensures that all operations are performed through a single shared instance, avoiding connection overhead and potential inconsistencies.

---

## Design Patterns Used

The architecture of PyME-Industrial is based on several classic design patterns, as illustrated in the provided diagrams:

### 1. **Singleton Pattern**

- **Purpose**: Ensures a single instance of the database manager (`DBManager`) is used throughout the application.
- **Benefit**: Prevents resource overuse and maintains data consistency.

### 2. **Template Method Pattern**

- **Purpose**: Provides a common structure for database operations (such as saving, loading, and updating requests) while allowing specific details to be defined by each request type (`DBSupply`, `DBThirdPartyServices`).
- **Benefit**: Reduces code duplication and increases maintainability.

### 3. **Simple Factory Method Pattern**

- **Purpose**: Centralizes the creation of different types of requests, ensuring they are properly initialized and configured.
- **Benefit**: Simplifies object creation and enforces consistency.

### 4. **Observer Pattern**

- **Purpose**: Allows users (observers) to subscribe to requests and receive notifications when their state changes.
- **Benefit**: Decouples notification logic from core business logic, making it easy to add or remove notification channels.

### 5. **State Pattern**

- **Purpose**: Encapsulates the various states of a request and their transitions, ensuring that each state handles its own behavior and transitions.
- **Benefit**: Makes the lifecycle management of requests clear, extensible, and robust.

---

## System Architecture

The system is organized into several modules:

- **Core Entities**: `Supply`, `ThirdPartyServices`, both inheriting from a common `Item` class.
- **Repositories**: Handle persistence and retrieval of requests.
- **Database Layer**: Manages all database operations through a singleton manager.
- **State Management**: Each request maintains its own state, with transitions managed via the state pattern.
- **Notification System**: Observers are notified of state changes using the observer pattern.

---

## Summary

PyME-Industrial provides a robust, extensible, and maintainable solution for managing procurement requests in an industrial SME context. By leveraging classic design patterns, it ensures clear separation of concerns, easy extensibility, and reliable operation, addressing the real-world needs of industrial purchasing departments.

---
