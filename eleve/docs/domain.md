# Domain Elements

## Annotation

- Definition: A string of text that holds some information about the object it is attached
- Attributes:
    - annotation_id
    - name
    - text
    - parent_id
    - parent_type
- Types: No types
- Status: No status
- Lifecycle: No lifecycle
- Relations:
    - Can be part of Task, CheckList, Plan and Project [many Annotations]
    - Can have Tags [1 Annotation - * Tags]
- Custom functionality:
    - Files: Annotations can hold FilePaths (images, spreadsheets, text files, any
    type of files, in fact) and it is aware of how many files it has.


## Tag

- Definition: A marker that represent a topic the object is connected with;
- Attributes:
    - tag_id
    - name
    - description
- Types: No types
- Status: No status
- Lifecycle: No lifecycle
- Relations:
    - Can be part of Task, Checklist, Plan and Project [many Tags]


## Cycles

- Definition: Represent time tracking objects for the tasks
- Attributes:
    - cycle_id
    - cycle_type
    - start_date
    - finish_date
    - max_time
    - current_time
    - id_cycle_log
    - status
- Types: no types
- Status: Draft, Ongoing, Paused, Finished
- Lifecycle:
    - Cycle is created [Draft]
    - Cycle is started one time [Ongoing]
    - Cycle is paused [Paused]
    - Cycle is finished [Finished]
- Relations:
    - Can be a part of a Task (1 Task - * Cycle)
- Custom Functionality:
    - Can be reseted (goes back to Draft status)

## Cycle Log

- Definition: Represent all state changes for a cycle
- Attributes:
    - cycle_log_id
    - cycle_id
    - previous_status
    - current_status
    - change_datetime
- Types: no types
- Status: no status
- Lifecycle: no lifecycle
- Relations:
    - A Cycle can have many Cycle Logs [1 Cycle - * Cycle Logs]

## Task

- Definition: A task is the minimum unity of work, an step to solve a larger problem;
- Attributes:
    - task_id
    - name
    - predicted_cycles
    - executed_cycles
    - due_date
    - start_date
    - finish_date
    - finished
    - status
- Types: No types
- Status: Draft, Ongoing, Finished;
- Lifecycle:
    - Task is created [Draft]
    - Task Cycle was started [Ongoing]
    - Task is marked as finished [Finished]
- Relations:
    - Can have a group of Annotations [1 Task - * Annotation];
    - Can be part of a CheckList;
    - Can have Tags [1 Task - * Tags]
- Implementation details:
    - A Task can be part of only one CheckList
- Custom Functionality:
    - Cycles: configurable timers for work and rest tracking (like Pomodoros, but 
    let's not use this name to avoid copyright);

## CheckList

- Definition: A larger problem that need many steps to be solved;
- Attributes:
    - checklist_id
    - name
    - due_date
    - start_date
    - finish_date
    - status
- Types: No types
- Status: Draft, Ongoing, Finished;
- Lifecycle:
    - CheckList is created [Draft]
    - A Task inside the CheckList was started [Ongoing]
    - All Tasks inside the CheckList was completed [Finished]
- Relations:
    - Can have a group of Annotations [1 CheckList - * Annotations];
    - Can have a group of Tasks [1 CheckList - * Tasks];
    - Can be part of a Plan [1 Plan - * CheckLists];
    - Can have Tags [1 CheckList - * Tags]
- 

## Plan

- Definition: Is an structure that represent the way we will solve a Project;
- Attributes:
    - id_plan
    - name
    - description
    - due_date
    - start_date
    - finish_date
    - plan_type
    - status
- Types: Continuous or Linear
- Status:
    - Linear: Draft, Ongoing, Finished, Closed;
- Lifecycle:
    - Continuous:
        - Continuous Plan is created [Draft]
        - Continuous Plan is being structured [Draft]
        - An activity in a CheckList has its Cycle started [Implemented]
        - Continuous Plan have its CheckLists finished and given more CheckLists [Implement]
        - Continuous Plan is discontinued [Closed]
        - Note: a Continuous Plan never finishes. A good example: support being given to an app (it is continuous)
    - Linear: 
        - Linear Plan is created [Draft]
        - Linear Plan is being structured [Draft]
        - An activity in a CheckList has its Cycle started [Ongoing]
        - Linear Plan have its CheckLists finished and given more CheckLists [Ongoing]
        - Linear Plan is finished [Finished]
        - Linear Plan is discontinued [Closed]
- Relations:
    - Can have a group of Annotations [1 Plan - * Annotation];
    - Should have a group of CheckLists [1 Plan - * CheckList];
    - Can have Tags [1 Plan - * Tags]
    - Can have a group of Milestones;
    - Is part of a Project;

## Milestone

- Definition: Represents a relevant point to be achieve in a plan
- Attributes:
    - milestone_id
    - name
    - due_date
    - achieved_date
    - status
- Types: No types
- Status: Not-Achieved and Achieved
- Lifecycle:
    - Milestone is created [Not-Achieved]
    - Milestone is attached to a plan [Not-Achieved]
    - Milestone is achieved [Achieved]
- Relations:
    - Part of a Plan

## Project

- Definition: Represents a major endeavor, that needs to be finished or be maintened.
- Attributes:
    - project_id
    - name
    - description
    - due_date
    - start_date
    - finish_date
    - project_config_id
    - status
- Types: No types
- Status: Draft, Ongoing, Finished, Closed 
- Lifecycle:
    - Project is created [Draft]
    - Project is being structured [Draft]
    - Project receives a Continuous Plan [Ongoing]
    - Project receives a Linear Plan [Ongoing]
    - All Linear Plans are finished and no Continuous Plan is present [Finished]
    - Project is discontinued [Closed]
- Relations:
    - Should have a Plan [1 Project - * Plans]
    - Is part of a Vault [1 Vault - * Projects]
    - Can have Tags [1 Project - * Tags]


## Project Configuration

- Definition: all values for Project configuration
- Attributes:
    - project_config_id
    - project_id
    - df_maxtime_work_cycle
    - df_maxtime_rest_cycle
    - df_maxtime_great_rest_cycle
    - df_qt_cycles_great_rest
    - predicted_cycles_per_day
- Types: no types
- Status: no status
- Lifecycle: no lifecycle
- Relations:
    - A Project has one configuration [1 Project - 1 Project Configuration]

## Vault

- Definition: Represents a virtual space where the user store Projects
- Attributes:
    - vault_id
    - name
    - description
- Types: No types
- Status: No status
- Relations:
    - Can have Projects [1 Vault - * Projects]

