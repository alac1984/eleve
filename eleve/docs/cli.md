# CLI Commands

The **eleve** CLI allows you to efficiently manage the system's primary entities, such as **Annotations**, **Tasks**, **CheckLists**, **Plans**, **Milestones**, and **Projects**. Additionally, it offers functionalities to manage work cycles related to **Tasks**.

## General Command Structure

```shell
eleve <command> <subcommand> [options]
```

- **command**: Main command group (`entity`, `cycle`, etc.).
- **subcommand**: Specific action to execute (`create`, `append`, `update`, etc.).
- **options**: Additional flags or parameters that modify the command's behavior.

---

## Entity Commands (`entity`)

Manage the primary entities of **eleve**, including creation, updating, appending, and listing.

### 1. Create Entity

Create a new entity in the system.

#### **Usage**

```shell
eleve entity create <type> <name> [--description <description> | -d <description>]
```

#### **Description**

Creates a new entity of the specified type with the provided name. The description is optional.

#### **Available Entity Types**

- `annotation`
- `task`
- `checklist`
- `plan`
- `milestone`
- `project`

#### **Examples**

```shell
eleve entity create task "Check priorities"
eleve entity create project "Eleve Development" --description "Project to develop the Eleve platform."
```

#### **Options**

- `--description <description>`, `-d <description>`: Defines a description for the entity.

---

### 2. Append Entity

Attach an existing entity to another target entity.

#### **Usage**

```shell
eleve entity append <ITEM_ID> <TARGET_ID>
```

#### **Description**

Attaches an existing entity (`ITEM_ID`) to a target entity (`TARGET_ID`).

#### **Examples**

```shell
eleve entity append e90b8831a4b8 00c6131c5e30
```

---

### 3. Update Entity

Update a specific attribute of an existing entity.

#### **Usage**

```shell
eleve entity update <ID> --attrib <attribute> <value> | -a <attribute> <value>
```

#### **Description**

Updates the specified attribute of an entity with the new provided value.

#### **Examples**

```shell
eleve entity update e90b8831a4b8 --attrib predicted_cycles 4
eleve entity update e90b8831a4b8 -a status "Finished"
```

#### **Options**

- `--attrib <attribute>`, `-a <attribute>`: Specifies the attribute to update and its new value.

---

### 4. Show Entity

Display details of a specific entity, with options to truncate IDs and omit relations.

#### **Usage**

```shell
eleve entity show <ID> [--no-trunc | -n] [--no-relations | -N]
```

#### **Description**

Displays comprehensive information about an entity, including its attributes and relations. Options allow control over ID truncation and the inclusion of relations.

#### **Examples**

```shell
eleve entity show e90b8831a4b8
eleve entity show e90b8831a4b8 --no-trunc
eleve entity show e90b8831a4b8 --no-relations
```

#### **Options**

- `--no-trunc`, `-n`: Displays the full ID of the entity without truncating.
- `--no-relations`, `-N`: Omits the display of the entity's relations.

---

### 5. List Entities

Display a list of entities of the specified type, with various options to filter and format the output.

#### **Usage**

```shell
eleve entity list <type> [--all | -A] [--limit <number> | -l <number>] [--related-to <ID> | -R <ID>] [--with-descriptions | -W] [--no-trunc | -n]
```

#### **Description**

Lists entities of the specified type, showing their IDs, names, and some attributes. Options allow filtering, limiting the number of results, and controlling the display of descriptions and ID truncation.

#### **Available Entity Types**

- `annotation`
- `task`
- `checklist`
- `plan`
- `milestone`
- `project`

#### **Examples**

```shell
eleve entity list annotation --limit 20
eleve entity list project --related-to e90b8831a4b8
eleve entity list task --with-descriptions
```

#### **Options**

- `--all`, `-A`: Lists all entities, including those that are completed or closed.
- `--limit <number>`, `-l <number>`: Limits the number of entities displayed.
- `--related-to <ID>`, `-R <ID>`: Filters entities related to a specific entity ID.
- `--with-descriptions`, `-W`: Includes entity descriptions in the listing.
- `--no-trunc`, `-n`: Displays the full IDs of entities without truncating.

---

## Cycle Commands (`cycle`)

Manage work cycles associated with **Tasks**, allowing you to start, stop, view, and modify cycles.

### 1. Start Cycle

Initiate a new work cycle for a specific **Task**.

#### **Usage**

```shell
eleve cycle <TASK_ID> start [--work | -w] [--rest | -r] [--rest-after | -f]
```

#### **Description**

Starts a work cycle for the specified **Task**. You can specify whether the cycle is for work or rest. With --rest-after, a rest cycle will start right after an work cycle has finished.

#### **Examples**

```shell
eleve cycle e90b8831a4b8 start --work
eleve cycle e90b8831a4b8 start -r
```

#### **Options**

- `--work`, `-w`: Initiates a work cycle.
- `--rest`, `-r`: Initiates a rest cycle.
- `--rest-after`, `-f`: A rest cycle starts right after a work cycle is done.

---

### 2. Stop Cycle

Stop the currently ongoing work cycle for a specific **Task**.

#### **Usage**

```shell
eleve cycle <TASK_ID> stop
```

#### **Description**

Stops the ongoing work cycle for the specified **Task**.

#### **Examples**

```shell
eleve cycle e90b8831a4b8 stop
```

---

### 3. Show Current Cycle

Display information about the current work cycle of a specific **Task**.

#### **Usage**

```shell
eleve cycle <TASK_ID> current
```

#### **Description**

Shows details of the ongoing work cycle for the specified **Task**.

#### **Examples**

```shell
eleve cycle e90b8831a4b8 current
```

---

### 4. Show Next Cycles

Display information about the upcoming planned work cycles for a specific **Task**.

#### **Usage**

```shell
eleve cycle <TASK_ID> next
```

#### **Description**

Shows details of the next planned work cycles for the specified **Task**.

#### **Examples**

```shell
eleve cycle e90b8831a4b8 next
```

---

### 5. Finish Cycle

Mark the current work cycle as finished, even if the planned time was not completed.

#### **Usage**

```shell
eleve cycle <TASK_ID> finish
```

#### **Description**

Ends the ongoing work cycle for the specified **Task**, regardless of whether it was completed as planned.

#### **Examples**

```shell
eleve cycle e90b8831a4b8 finish
```

---

### 6. Change Next Cycle

Modify the next work cycle to be a work cycle.

#### **Usage**

```shell
eleve cycle <TASK_ID> change
```

#### **Description**

Changes the upcoming work cycle to a work cycle, adjusting as necessary.

#### **Examples**

```shell
eleve cycle e90b8831a4b8 change
```

---

## Additional Commands

### 1. Import

Import entity or configuration data from a JSON file.

#### **Usage**

```shell
eleve import <path> [--create-all,-C] [--just-config,-j]
```

#### **Description**

Imports entity or configuration data from a file located at the specified path. The expected format is JSON. If the entities in the file have IDs and these IDs were found in the database, they will be updated. If the --create-all option is provided, IDs will be ignored, and all entities will be created as new. If --just-config is passed on, only configuration data will be imported.

#### **Examples**

```shell
eleve import ~/files/project.json
eleve import C:\eleve\myplans\project.json --just-config
```

---

### 4. Export

Export entity data to a file.

#### **Usage**

```shell
eleve export <ID> [--no-relations | -N]
```

#### **Description**

Exports the specified entity's data to a JSON file, with an option to omit relations.

#### **Examples**

```shell
eleve export e90b8831a4b8
eleve export e90b8831a4b8 --no-relations
```

#### **Options**

- `--no-relations`, `-N`: Omits the inclusion of relations in the exported file.

---
