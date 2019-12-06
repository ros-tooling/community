# ROS 2 Tooling Working Group

The Tooling Working Group's mission is to provide ROS2 users with simple, robust and easy to use tools for recording, debugging, visualization and introspection purposes.

This document is a first and limited draft of the scope and governance of the ROS 2 Tooling Working Group.

## Meetings

* Regular WG Meeting: Every other Friday at 9:00 PT (Pacific Time) (biweekly).
    * Meeting notes and Agenda.
    * Meeting recordings

## Subprojects

The following subprojects are owned by Tooling WG:
* system_metrics_collector
* cross_compile
* rosbag2
* file_talker
* GitHub Actions for CI on WG Subprojects
    * action-ros2-ci
    * action-ros2-lint
    * setup-ros2
    * action-amazon-chime
    * action-pypi

### Adding new subprojects

To request introduction of a new subproject, use the appropriate issue template on this repository to create a request.

The full process for introducing new subprojects to the WG is being discovered, requests will be discussed at the regularly scheduled meetings.

### Standards for subprojects

When adopting a subproject, the WG agrees that a specific set of criteria will be maintained by the WG.

These criteria are:
* Build passes against ROS2 master
* The ROS2 standard linter set is enabled and adhered to
* Builds have 0 warnings
* Quality builds are green (address sanitizer, thread sanitizer, clang thread safety analysis)
* Test suite passes
* Reasonable* code coverage is met by test suites
* Issues are responded to promptly*
* Releases go out regularly* when bugfixes or new features are introduced

\* - Precise definition of term not determined

## Scope

WG Tooling’s mission is to provide ROS2 users with simple, robust and easy to use tools for recording, debugging, visualization and introspection purposes.

### In scope

* Subprojects owned by the WG

### Out of scope

* Middleware/communications

## Membersip, Roles and Organization Management

The roles of the WG are reflected in its Teams

* Members
    * Issue triage privileges
* Reviewers
    * Code review privileges
* Approvers
    * Code review approval and merge privileges
* Subproject owner
    * Admin on a specific subproject

To become a member or change role, use the appropriate issue template on this repository to create a request.
